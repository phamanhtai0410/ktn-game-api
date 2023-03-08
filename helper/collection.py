# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import sentry_sdk
from pydash import get

from connect import dlm
from models import CollectionModel
from pydash import get
from enums import CollectionDefault


class CollectionHelper:
    @staticmethod
    def get_msg(amount, timestamp, event):
        return f"I exchange {amount} points from '{event}' event of Katana to {amount} USDT at {timestamp} seconds timestamp."

    @staticmethod
    def lock_address(address):
        try:
            _lock = dlm.lock(f'ktn:redlock:exchange:{address}', 60 * 1000)  # 1 minute
            if _lock:
                return True

        except:
            sentry_sdk.capture_exception()
        return False

    @staticmethod
    def handle_submitted_game_item(form_data):
        try:
            _item0 = get(form_data, "types_list")[0]
            _itemID = get(_item0, "DataTableID")
            _description = get(_item0, "AssetDescription")
            _types_list = get(form_data, "types_list")
            _types_list_added_rate = [
                {
                    **_type,
                    "rate": 100 / len(_types_list)
                }
                for _type in _types_list
            ]

            _collections = list(CollectionModel.find(filter={}))
            _max_id = max([get(_item, "collection_id") for _item in _collections])

            CollectionModel.insert_one(
                row={
                    "collection_id": _max_id + 1,
                    "name": get(form_data, "item_name"),
                    "symbol": f"KTN_{_itemID}",
                    "description": _description,
                    "types_list": _types_list_added_rate,
                    "deployed": False,
                    # Royalty
                    "royalty_rate": CollectionDefault.ROYALTY_RATE,
                    # Total Supply
                    "total_supply": CollectionDefault.TOTAL_SUPPLY,
                    "created_by": "game@launcher"
                }
            )
            return True
        except Exception as e:
            print(e)
            sentry_sdk.capture_exception()
        return False
