# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from config import Config
from lib import AsyncDaoModel, DaoModel
from connect import connect_db, redis_cluster
from .collection import CollectionDao


__models__ = [
    'CollectionModel'
]

CollectionModel = CollectionDao(
    connect_db.db.collection,
    redis=redis_cluster,
    broker=Config.BROKER_URL
)


