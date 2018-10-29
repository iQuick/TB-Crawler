#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/12/11

import logging
import logging.config
from datetime import datetime

logging.config.fileConfig("./conf/logging.conf")  # 采用配置文件

# create logger
logger = logging.getLogger("simpleExample")

