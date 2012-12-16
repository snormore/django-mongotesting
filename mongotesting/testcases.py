#coding: utf-8
from nose.plugins.skip import SkipTest

from mongoengine.python_support import PY3
from mongoengine import connect

try:
    from django.test import TestCase
    from django.conf import settings
except Exception as err:
    if PY3:
        from unittest import TestCase
        # Dummy value so no error
        class settings:
            MONGO_DATABASE_NAME = 'dummy'
    else:
        raise err


class MongoTestCase(TestCase):
    """
        TestCase class that clear the collection between the tests
    """
    
    def _pre_setup(self):
        if PY3:
            raise SkipTest('django does not have Python 3 support')

        from mongoengine.connection import connect, disconnect, get_connection
        for db_name, db_alias in settings.MONGO_DATABASES.items():
            connection = get_connection(db_alias)
            connection.drop_database(db_name)
            disconnect(db_alias)
            connect(db_name, port=settings.MONGO_PORT)
        super(MongoTestCase, self)._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        for db_name, db_alias in settings.MONGO_DATABASES.items():
            connection = get_connection(db_alias)
            connection.drop_database(db_name)
            disconnect(db_alias)
        super(MongoTestCase, self)._post_teardown()

