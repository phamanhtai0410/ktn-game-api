from lib.exception import BadRequest

class TooLongItemList(Exception):
    def __init__(self, msg="Item list is too long (just max 10 each time)", *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.status_code = 400
        self.msg = msg
        self.errors = kwargs.get('errors', [])
        self.error_code = 'E_ITEM_LIST_TOO_LONG_CODE'

    pass