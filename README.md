django-mongotesting
===================

An extension to the Django web framework that provides testing support for mongoengine dependent modules.


Usage
=====

First, define MONGO_DATABASE_NAME and MONGO_PORT settings. Including the mongo connection bit, you should have something like this in your settings.py file:

    MONGO_DATABASE_NAME = 'fooproject'
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    import mongoengine
    mongoengine.connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)

If you would like a test mongo db created and destroyed for each test method in a class then inherit the MongoTestCase class from mongotesting.testcases.

If you would like a test mongo db created and destroyed for each test class, then define the TEST_RUNNER setting to use MongoTestRunner, as follows:

    TEST_RUNNER = 'mongotesting.testrunners.MongoTestRunner'

