from tests.test_base import TestBase
import os
import inspect
from os.path import dirname
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(parentdir)

class User:

    '''
    Constructor which assign all fields. Some fields can have default value.
    '''
    def __init__(self, email = TestBase.data()['existing_login'], password = TestBase.data()['existing_password']):
    
        if email == None:
            self._email = TestBase.data()['existing_login']
        else:
            self._email = email
        if password == None:
            self._password = TestBase.data()['existing_password']
        elif password == "WRONG":
            self._password = TestBase.data()['not_existing_password']
        else:
            self._password = password

