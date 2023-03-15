# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from pydash import get

from lib import DaoModel

class AdminDefaultConfigsDao(DaoModel):
    def __init__(self, *args, **kwargs):
        super(AdminDefaultConfigsDao, self).__init__(*args, **kwargs)
        