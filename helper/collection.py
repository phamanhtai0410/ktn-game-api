# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import sentry_sdk
from pydash import get

from connect import dlm
from models import CollectionModel, AdminDefaultConfigsModel
from pydash import get
from enums import CollectionDefault
from exceptions.collection import TooLongItemList


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
        print(form_data)
        try:
            _items = get(form_data, "items")
            if len(_items) > 10:
                raise TooLongItemList
            for _item in _items:
                # Parse data from json
                _item_types = get(_item, "types_list")
                _item_name = get(_item, "item_name")
                _category = get(_item, 'category', 'Character')
                _chain = get(_item, 'chain', 'BSC')

                _type0 = _item_types[0]
                _itemID = get(_type0, "DataTableID")
                _description = get(_type0, "AssetDescription")

                # Add rate for the types list
                _types_list_added_rate = [
                    {
                        **_type,
                        "rate": 100 / len(_item_types)
                    }
                    for _type in _item_types
                ]

                # Add default Price
                _default_price = get(AdminDefaultConfigsModel.find_one(filter={
                    'type': 'NFT',
                    'name': 'PRICE'
                }), "value", CollectionDefault.PRICE)

                _types_list_added_price = [
                    {
                        **_type,
                        "price": _default_price
                    } for _type in _types_list_added_rate
                ]

                # Increase Max_id for `collection_id`
                _collections = list(CollectionModel.find(filter={}))
                _max_id = max([get(_item, "collection_id") for _item in _collections])

                # Load default configs's value in the current state of the system
                _total_supply_default = get(AdminDefaultConfigsModel.find_one(filter={
                    'type': 'NFT',
                    'name': 'TOTAL_SUPPLY'
                }), "value", CollectionDefault.TOTAL_SUPPLY)

                _royalty_rate_default = get(AdminDefaultConfigsModel.find_one(filter={
                    'type': 'ROYALTY',
                    'name': 'RATE'
                }), "value", CollectionDefault.ROYALTY_RATE)

                _commision_default = get(AdminDefaultConfigsModel.find_one(filter={
                    'type': 'NFT',
                    'name': 'COMMISSION'
                }), "value", CollectionDefault.COMMISSION)
                
                _commision_level_2_default = get(AdminDefaultConfigsModel.find_one(filter={
                    'type': 'NFT',
                    'name': 'COMMISSION'
                }), "value", CollectionDefault.COMMISSION_LEVEL_2)

                # Create a record of new `DRAFT` collection
                CollectionModel.insert_one(
                    row={
                        "collection_id": _max_id + 1,
                        "name": _item_name,
                        "symbol": f"KTN_{_itemID}",
                        "description": _description,
                        "category": _category,
                        "commission": float(_commision_default),
                        "commission_level_2": float(_commision_level_2_default),
                        "chain": _chain,
                        "types_list": _types_list_added_price,
                        "deployed": False,
                        # Royalty
                        "royalty_rate": int(_royalty_rate_default),
                        # Total Supply
                        "total_supply": int(_total_supply_default),
                        "created_by": "game@launcher"
                    }
                )
            return True
        except Exception as e:
            print(e)
            sentry_sdk.capture_exception()
        return False
