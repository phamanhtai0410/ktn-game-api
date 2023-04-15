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
    AssetDescription = fields.Str(missing='')
    AssetRarity = fields.Str(required=True)
    AssetUniqueIndex = fields.Str()
    AnimationModelUrl = fields.Str()
    ImageUrl = fields.Str()

class ItemDetail(Schema):
    class Meta:
        unknown = INCLUDE
    
    item_name = fields.Str(required=True)
    category = fields.Str(default='character')
    chain = fields.Str()
    types_list = fields.List(fields.Nested(PropertiesSchema), required=True)
    
class CollectionSubmitForm(Schema):
    class Meta:
        unknown = INCLUDE
    
    items = fields.List(fields.Nested(ItemDetail), required=True)

   

