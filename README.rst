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

    #!/usr/bin/env python3
    from sanic import Sanic, response
    from sanic_mongodb_ext import MongoDbExtension
    from umongo import Instance, Document, MotorAsyncIOInstance
    from umongo.fields import StringField


    app = Sanic(__name__)
    # Configuration for MongoDB and uMongo
    app.config.update({
        "MONGODB_DATABASE": "app", # Make ensure that the `app` database is really exists
        "MONGODB_URI": "mongodb://root:root@mongodb:27017",
        # You can also specify custom connection options.
        # For more details check the official docs: https://api.mongodb.com/python/3.7.0/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
        "MONGODB_CONNECT_OPTIONS: {
            "minPoolSize": 10,
            "maxPoolSize": 50,
        },
        "LAZY_UMONGO": MotorAsyncIOInstance(),
    })
    # uMongo client is available as `app.mongodb` or `app.extensions['mongodb']`.
    # The lazy client will be available as `app.lazy_mongodb` only when the database was specified,
    # and which is a great choice for the structured projects.
    MongoDbExtension(app)


    # Describe the model
    @app.lazy_umongo.register
    class Artist(Document):
        name = StringField(required=True, allow_none=False)


    # And use it later for APIs
    @app.route("/")
    async def handle(request):
        artist = Artist(name="A new rockstar!")
        await artist.commit()
        return response.json(artist.dump())


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)

License
=======
The sanic-mongodb-extension is published under BSD license. For more details read LICENSE_ file.

.. _links:
.. _uMongo: https://github.com/Scille/umongo
.. _motor_asyncio: https://motor.readthedocs.io/en/stable/
.. _LICENSE: https://github.com/Relrin/sanic-mongodb-extension/blob/master/LICENSE

Real project examples
=====================
Open Matchmaking project:  

- `Auth/Auth microservice <https://github.com/OpenMatchmaking/microservice-auth/>`_
- `Game servers pool microservice <https://github.com/OpenMatchmaking/microservice-game-servers-pool/>`_
- `Player statistics microservice <https://github.com/OpenMatchmaking/microservice-player-statistics/>`_
