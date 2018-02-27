sanic-mongodb-extension
#######################
MongoDB with μMongo ODM support for Sanic framework

Features
========
- Uses motor_asyncio_ package for async queries to MongoDB
- Good integrated with uMongo_ ODM, so that you can use it easily in your projects

Installation
============
This package should be installed using pip: ::

    pip install sanic-mongodb-extension

Example
=======
.. code-block:: python

    from sanic import Sanic, response
    from sanic_mongodb_ext import MongoDbExtension
    from umongo import Document, MotorAsyncIOInstance
    from umongo.fields import StringField


    app = Sanic(__name__)
    # Configuration for MongoDB and uMongo
    app.config.update({
        "MONGODB_DATABASE": "example_database",
        "MONGODB_URI": "mongodb://user:password@mongodb:27017",
        "LAZY_UMONGO": MotorAsyncIOInstance(),
    })
    MongoDbExtension(app) # uMongo client is available as `app.mongodb` or `app.extensions['mongodb']`
    instance = app.config["LAZY_UMONGO"]  # For a structured applications the lazy client very useful


    # Describe the model
    @instance.register
    class Artist(Document):
        name = StringField(required=True, allow_none=False)


    # And use it later for APIs
    @app.route("/")
    async def handle(request):
        artist = Artist(name="A new rockstar!")
        await artist.commit()
        return response.json(artist.dump())

License
=======
The sanic-mongodb-extension is published under BSD license. For more details read LICENSE_ file.

.. _links:
.. _uMongo: https://github.com/Scille/umongo
.. _motor_asyncio: https://motor.readthedocs.io/en/stable/
.. _LICENSE: https://github.com/Relrin/sanic-mongodb-extension/blob/master/LICENSE
