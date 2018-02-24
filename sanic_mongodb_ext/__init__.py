__version__ = '0.1.1'
__all__ = ['MongoDbExtension', ]

VERSION = __version__


from motor.motor_asyncio import AsyncIOMotorClient
from sanic_base_ext import BaseExtension


class MongoDbExtension(BaseExtension):
    extension_name = app_attribute = 'mongodb'

    def init_app(self, app, *args, **kwargs):
        super(MongoDbExtension, self).init_app(app, *args, **kwargs)

        @app.listener('before_server_start')
        async def mongodb_configure(app_inner, _loop):
            client = AsyncIOMotorClient(app_inner.config['MONGODB_URI'])
            setattr(app_inner, self.app_attribute, client)

            if not hasattr(app, 'extensions'):
                setattr(app, 'extensions', {})
            app.extensions[self.extension_name] = client

            database = app_inner.config['MONGODB_DATABASE']
            if database:
                motor_database_client = client[database]
                lazy_instance = app_inner.config['LAZY_UMONGO']
                lazy_instance.init(motor_database_client)

        @app.listener('after_server_stop')
        async def mongodb_free_resources(app_inner, _loop):
            client = getattr(app_inner, self.app_attribute, None)

            if client:
                client.close()
