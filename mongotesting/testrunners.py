#coding: utf-8
from django.test.simple import DjangoTestSuiteRunner
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

class MongoTestRunner(DjangoTestSuiteRunner):
    """
        A test runner that can be used to create, connect to, disconnect from, 
        and destroy a mongo test database for standard django testing.

        NOTE:
            The MONGO_PORT and MONGO_DATABASE_NAME settings must exist, create them
            if necessary.
    """

    def __init__(self, *args, **kwargs):
        if hasattr(settings, 'MONGO_DATABASE_NAME'):
            mongodb_name = 'test_%s' % settings.MONGO_DATABASE_NAME
        else:
            mongodb_name = None
        if hasattr(settings, 'MONGO_DATABASES'):
            mongodb_names = ['test_%s' % (db_name, ) for db_name in settings.MONGO_DATABASES.keys()]
        else:
            mongodb_names = []
        if mongodb_name:
            mongodb_names.append(mongodb_name)
        if not mongodb_names:
            print '* Warning: no mongodb specified in settings using MONGO_DATABASE_NAME or MONGO_DATABASES.'
        self.mongodb_names = mongodb_names
        super(MongoTestRunner, self).__init__(*args, **kwargs)

    def setup_databases(self, **kwargs):
        from mongoengine.connection import connect, disconnect
        for db_name in self.mongodb_names:
            disconnect(db_name)
            connect(db_name, port=settings.MONGO_PORT)
            print 'Creating mongo test database ' + db_name
        return super(MongoTestRunner, self).setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        from mongoengine.connection import get_connection, disconnect
        for db_name in self.mongodb_names:
            connection = get_connection(db_name)
            connection.drop_database(db_name)
            print 'Dropping mongo test database: ' + db_name
            disconnect(db_name)
        super(MongoTestRunner, self).teardown_databases(old_config, **kwargs)

