# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.collection import CollectionResource, ExistingMetadataResource

api_resources = {
    '/health_check': HealthCheck,
    "/collection": CollectionResource,
    "/collection/existing_metadata": ExistingMetadataResource
}
