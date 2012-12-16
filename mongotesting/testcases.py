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

    def __init__(self, *args, **kwargs):
        if hasattr(settings, 'MONGO_DATABASE_NAME'):
            mongodb_name = 'test_%s' % settings.MONGO_DATABASE_NAME
        else:
            mongodb_name = None
        if hasattr(settings, 'MONGO_DATABASES'):
            mongodb_names = ['test_%s' % (db_name, ) for db_name in settings.MONGO_DATABASES]
        else:
            mongodb_names = []
        if mongodb_name:
            mongodb_names.append(mongodb_name)
        if not mongodb_names:
            print '* Warning: no mongodb specified in settings using MONGO_DATABASE_NAME or MONGO_DATABASES.'
    
    def _pre_setup(self):
        if PY3:
            raise SkipTest('django does not have Python 3 support')

        from mongoengine.connection import connect, disconnect, get_connection
        for db_name in self.mongodb_names:
            connection = get_connection()
            connection.drop_database(db_name)
            disconnect()
            connect(db_name, port=settings.MONGO_PORT)
        super(MongoTestCase, self)._pre_setup()

    def _post_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        for db_name in self.mongodb_names:
            connection = get_connection()
            connection.drop_database(db_name)
            disconnect()
        super(MongoTestCase, self)._post_teardown()

