#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2017/12/13

_DEBUG = False
_VERSION = 'v0.8.0'
_USERNAME = 'xxxx'
_PASSWORD = 'xxxx'


def usage():
    """
    The output  configuration file contents.
    
    Usage: run.py [-d|--debug] [-h|--help] [-v|--version] [output, =[argument]]
    
    Description
                -d,--debug      debug mode.
                -h,--help       help doc.
                -v,--version    software version.
    for example:
        python run.py -d
    """


def get_username():
	return _USERNAME


def get_password():
	return _PASSWORD


def get_version():
    return _VERSION


def get_debug():
    return _DEBUG


def set_debug(debug):
    global _DEBUG
    _DEBUG = debug
    return _DEBUG
