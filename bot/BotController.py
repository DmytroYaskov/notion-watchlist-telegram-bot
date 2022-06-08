from TelegramAPIDecorator import APIBase
from message import Message

from DBController import DBController

# User context
# - ID
# - State
# - - name "state:substate"
# - - - can be used to load wanted handler after bot restart
# - - message handler 

# keys
# - key:userID

# States (1 User's Message - 1 State)
# - Start (default state for new users)
# - - Waiting for start command to process user access
# - Command (default for users, sets after Start and after some timeout of user inactivity)
# - Ignore (default for unallowed users, disables message handling and inactivity timeout)
# - - set message handler to None

class TelegramBotController():
    def __init__(self, api_provider: APIBase) -> None:

        self._db = DBController("bot.db");

        self._api_provider = api_provider
        self._api_provider.add_message_handler(self._message_handler)

        pass

    def _message_handler(self, chat_id: int, message: object) -> None:

        if !

        pass
