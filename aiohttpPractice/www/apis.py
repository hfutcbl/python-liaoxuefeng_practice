#! usr/bin/python3
# -*- coding:utf-8-*-

'''
JSON API definition
'''

import json, logging, inspect, functools


class APIError(Exception):
    '''
    the base APIError which contains error(required, data(optional), and message(optional))
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input from
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('Permission:forbidden', 'permission', message)