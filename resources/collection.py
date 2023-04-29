# -*- coding: utf-8 -*-
"""
   Description: The route for collection relevant actions
        -
        -
"""
from flask_restful import Resource
from connect import security
from helper.collection import CollectionHelper
from schemas.collection import CollectionSubmitForm, ExistingMetadataCollectionForm


class CollectionResource(Resource):

    @security.http(
        form_data=CollectionSubmitForm()
    )
    def post(self, form_data):
        _res = CollectionHelper.handle_submitted_game_item(form_data=form_data)
        return {
            'status': 'PROCESSING'
        }
        
class ExistingMetadataResource(Resource):
    @security.http(
        form_data=ExistingMetadataCollectionForm()
    )
    def post(self, form_data):
        _res = CollectionHelper.handle_existing_metadata_collection(form_data=form_data)
        return _res
