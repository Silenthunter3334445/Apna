
import asyncio

from pyrogram import Client
import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):
        self.one = self._make_client("NandAss1", config.STRING1)
        self.two = self._make_client("NandAss2", config.STRING2)
        self.three = self._make_client("NandAss3", config.STRING3)
        self.four = self._make_client("NandAss4", config.STRING4)
        self.five = self._make_client("NandAss5", config.STRING5)

    @staticmethod
    def _make_client(name, session_string):
        if not session_string:
            return None

        return Client(
            name=name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=session_string,
            no_updates=True,
        )

    async def get_bot_username_from_token(self, token):
        temp_bot = None
        try:
            temp_bot = Client(
                name="temp_bot",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=token,
                no_updates=True,
            )
            await temp_bot.start()
            me = await temp_bot.get_me()
            return me.username
        except Exception:
            LOGGER(__name__).exception(
                "Failed to get bot username"
            )
            return None
        finally:
            if temp_bot and temp_bot.is_connected:
                await temp_bot.stop()

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        log_group = getattr(config, "LOG_GROUP_ID", None)

        if not log_group:
            raise RuntimeError(
                "LOG_GROUP_ID is missing from Railway Variables/config.py"
            )

        bot_username = await self.get_bot_username_from_token(
            config.BOT_TOKEN
        )

        clients = [
            (1, self.one, "Assistant Account 1"),
            (2, self.two, "Assistant Account 2"),
            (3, self.three, "Assistant Account 3"),
            (4, self.four, "Assistant Account 4"),
            (5, self.five, "Assistant Account 5"),
        ]

        for number, client, label in clients:
            if client is None:
                LOGGER(__name__).info(
                    f"{label} skipped: STRING{number} is empty"
                )
                continue

            try:
                await client.start()

                me = await client.get_me()

                # Check that this assistant can access the log group.
                await client.send_message(
                    chat_id=log_group,
                    text=f"{label} started successfully."
                )

                client.id = me.id
                client.name = me.mention
                client.username = me.username

                assistants.append(number)
                assistantids.append(me.id)

                LOGGER(__name__).info(
                    f"{label} started as @{me.username or me.id}"
                )

            except Exception as e:
                LOGGER(__name__).error(
                    f"{label} failed. "
                    f"Exception: {type(e).__name__}: {e}"
                )

                # Stop the failed client cleanly.
                try:
                    if client.is_connected:
                        await client.stop()
                except Exception:
                    LOGGER(__name__).exception(
                        f"Failed to stop {label}"
                    )

                raise RuntimeError(
                    f"{label} could not access LOG_GROUP_ID. "
                    "Check the detailed error above."
                ) from e

        if not assistants:
            raise RuntimeError(
                "No assistant sessions are configured. "
                "Set at least one valid STRING1-STRING5."
            )

        if bot_username:
            await self.send_help_message(bot_username)

        await self.send_config_variables()

    async def send_help_message(self, bot_username):
        message = (
            f"@{bot_username} Successfully Started ✅\n\n"
            f"Owner: {config.OWNER_USERNAME}"
        )

        for number, client in [
            (1, self.one),
            (2, self.two),
            (3, self.three),
            (4, self.four),
            (5, self.five),
        ]:
            if number in assistants and client:
                try:
                    await client.send_message(
                        config.DT_Management, message
                    )
                    return
                except Exception:
                    LOGGER(__name__).exception(
                        "Could not send startup notification"
                    )

    async def send_config_variables(self):
        # Never send API_HASH, BOT_TOKEN, or session strings.
        message = (
            "<b>Assistant Status</b>\n\n"
            f"<b>Active sessions:</b> {', '.join(map(str, assistants))}\n"
            f"<b>Bot username:</b> @{config.BOT_USERNAME}\n"
            "<b>Secrets:</b> Hidden"
        )

        for number, client in [
            (1, self.one),
            (2, self.two),
            (3, self.three),
            (4, self.four),
            (5, self.five),
        ]:
            if number in assistants and client:
                try:
                    await client.send_message(
                        config.DT_Management, message
                    )
                    return
                except Exception:
                    LOGGER(__name__).exception(
                        "Could not send assistant status"
                    )

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")

        clients = [
            self.one,
            self.two,
            self.three,
            self.four,
            self.five,
        ]

        for client in clients:
            if client and client.is_connected:
                try:
                    await client.stop()
                except Exception:
                    LOGGER(__name__).exception(
                        "Failed to stop an assistant"
                    )

        assistants.clear()
        assistantids.clear()
        
