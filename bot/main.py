import asyncio
import logging

from aiotdlib import Client
from aiotdlib.api import API, BaseObject, UpdateNewMessage

async def main():
    client = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER
    )

    client.add_event_handler(any_event_handler, update_type=API.Types.UPDATE_NEW_MESSAGE)
    client.add_event_handler(update_chat_filters_handler, update_type=API.Types.UPDATE_CHAT_FILTERS)

    async with client:
        me = await client.api.get_me()
        logging.info(f"Successfully logged in as {me.json()}")
        await client.idle()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())