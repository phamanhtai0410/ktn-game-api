# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from pydash import get

from lib import DaoModel


class CollectionDao(DaoModel):
    def __init__(self, *args, **kwargs):
        super(CollectionDao, self).__init__(*args, **kwargs)
