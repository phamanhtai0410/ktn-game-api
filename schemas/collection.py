# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, EXCLUDE, fields, validate, INCLUDE

from lib import NotBlank

class PropertiesSchema(Schema):
    class Meta:
        unknown = INCLUDE

    DataTableID = fields.Str(required=True)
    EventDataTableID = fields.Str()
    AssetID = fields.Str(required=True)
    AssetDescription = fields.Str(required=True)
    AssetRarity = fields.Str(required=True)
    AssetUniqueIndex = fields.Str()
    AnimationModelUrl = fields.Str()
    ImageUrl = fields.Str()

class ItemDetail(Schema):
    class Meta:
        unknown = EXCLUDE
    
    item_name = fields.Str(required=True)
    types_list = fields.List(fields.Nested(PropertiesSchema), required=True)
    
class CollectionSubmitForm(Schema):
    class Meta:
        unknown = EXCLUDE
    
    items = fields.List(fields.Nested(ItemDetail), required=True)

   

