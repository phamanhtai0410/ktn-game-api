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
from .admin_default_configs import AdminDefaultConfigsDao


__models__ = [
    'CollectionModel',
    'AdminDefaultConfigsModel'
]

CollectionModel = CollectionDao(
    connect_db.db.collection,
    redis=redis_cluster,
    broker=Config.BROKER_URL
)

AdminDefaultConfigsModel = AdminDefaultConfigsDao(
    connect_db.db.admin_default_configs,
    redis=redis_cluster,
    broker=Config.BROKER_URL
)


