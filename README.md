django-mongotesting
===================

An extension to the Django web framework that provides testing support for mongoengine dependent modules.


Requirements
============

* Django 1.2+
* MongoEngine
* nose - https://github.com/nose-devs/nose

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


Reference
=========

* http://mongoengine.org/
* https://github.com/hmarr/mongoengine
* https://www.djangoproject.com/
* http://www.mongodb.org/
* https://gist.github.com/3760008
* https://github.com/hmarr/mongoengine/blob/master/mongoengine/django/tests.py
* https://groups.google.com/forum/?fromgroups=#!topic/mongoengine-dev/AKvPw3YJL9E
* http://bit.ly/PFKbZm
* http://nubits.org/post/django-mongodb-mongoengine-testing-with-custom-test-runner/
* http://nubits.org/post/django-mongodb-mongoengine-testing-with-a-custom-mongo-test-case/

