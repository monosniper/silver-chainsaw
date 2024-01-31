import schedule
import time
from telethon import TelegramClient

users = [
    {
        "api_id": 27532329,
        "api_hash": 'e261d20a94faacd382b439a91a76f343',  # +447501159303
    }
]


def spam():
    for user in users:
        client = TelegramClient(str(user["api_id"]), user["api_id"], user["api_hash"])

        async def main():
            me = await client.get_me()
            print('Connected to ' + me.username)

            async for dialog in client.iter_dialogs():
                print("Sent to " + dialog.name)
                try:
                    await client.send_message(dialog.id, 'Привет')
                except Exception:
                    print('Can\'t send, this is a channel')
                # print('Connected to ' + me.username)

        with client:
            client.loop.run_until_complete(main())


schedule.every().hour.do(spam)

while True:
    schedule.run_pending()
    time.sleep(1)

# message = await client.send_message(
#     'me',
#     'This message has **bold**, `code`, __italics__ and '
#     'a [nice website](https://example.com)!',
#     link_preview=False
# )
