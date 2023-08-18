import asyncio
import logging

from ouija import StreamTuning, DatagramTuning, StreamTelemetry, DatagramTelemetry, StreamRelay, DatagramRelay

import settings
from settings import Protocol


logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG if settings.DEBUG else logging.ERROR,
)


async def main() -> None:
    match settings.PROTOCOL:
        case Protocol.TCP:
            tuning = StreamTuning(
                fernet=settings.fernet,
                token=settings.TOKEN,
                serving_timeout=settings.SERVING_TIMEOUT,
                tcp_buffer=settings.TCP_BUFFER,
                tcp_timeout=settings.TCP_TIMEOUT,
                message_timeout=settings.MESSAGE_TIMEOUT,
            )
            relay = StreamRelay(
                telemetry=StreamTelemetry(),
                tuning=tuning,
                proxy_host=settings.PROXY_HOST,
                proxy_port=settings.PROXY_PORT,
            )

            if settings.MONITOR:
                asyncio.create_task(relay.debug())

            server = await asyncio.start_server(
                relay.serve,
                settings.RELAY_HOST,
                settings.RELAY_PORT,
            )
            async with server:
                await server.serve_forever()
        case Protocol.UDP:
            tuning = DatagramTuning(
                fernet=settings.fernet,
                token=settings.TOKEN,
                serving_timeout=settings.SERVING_TIMEOUT,
                tcp_buffer=settings.TCP_BUFFER,
                tcp_timeout=settings.TCP_TIMEOUT,
                udp_payload=settings.UDP_PAYLOAD,
                udp_timeout=settings.UDP_TIMEOUT,
                udp_retries=settings.UDP_RETRIES,
                udp_capacity=settings.UDP_CAPACITY,
                udp_resend_sleep=settings.UDP_RESEND_SLEEP,
            )
            relay = DatagramRelay(
                telemetry=DatagramTelemetry(),
                tuning=tuning,
                proxy_host=settings.PROXY_HOST,
                proxy_port=settings.PROXY_PORT,
            )

            if settings.MONITOR:
                asyncio.create_task(relay.debug())

            server = await asyncio.start_server(
                relay.serve,
                settings.RELAY_HOST,
                settings.RELAY_PORT,
            )
            async with server:
                await server.serve_forever()
        case _:
            raise NotImplementedError


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
