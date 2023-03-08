# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.collection import CollectionResource

api_resources = {
    '/health_check': HealthCheck,
    "/collection": CollectionResource
}
