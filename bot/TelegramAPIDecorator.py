from pyclbr import Function
from message import Message

class APIBase():
    def __init__(self) -> None:
        pass

    def add_message_handler(handler: Function) -> None:

        pass

    def send_message(message: Message) -> int:
        pass

    def update_message(message_id: int, updater: Function) -> None:
        pass

class TelegramAPI(APIBase):
    def __init__(self) -> None:
        super().__init__()


class APIMock(APIBase):
    def __init__(self) -> None:
        super().__init__()