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

    def setup_databases(self, **kwargs):
        from mongoengine.connection import connect, disconnect
        for db_name, db_alias in settings.MONGO_DATABASES.items():
            disconnect(db_alias)
            connect(db_name, port=settings.MONGO_PORT)
            print 'Creating mongo test database ' + db_name
        return super(MongoTestRunner, self).setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        from mongoengine.connection import get_connection, disconnect
        for db_name, db_alias in settings.MONGO_DATABASES.items():
            connection = get_connection(db_alias)
            connection.drop_database(db_name)
            print 'Dropping mongo test database: ' + db_name
            disconnect(db_alias)
        super(MongoTestRunner, self).teardown_databases(old_config, **kwargs)

