__version__ = '0.2.2'
__all__ = ['MongoDbExtension', ]

VERSION = __version__


from motor.motor_asyncio import AsyncIOMotorClient
from sanic_base_ext import BaseExtension


class MongoDbExtension(BaseExtension):
    extension_name = app_attribute = 'mongodb'
    lazy_app_attribute = 'lazy_umongo'

    def init_app(self, app, *args, **kwargs):
        super(MongoDbExtension, self).init_app(app, *args, **kwargs)

        lazy_instance = app.config.get('LAZY_UMONGO', None)
        if lazy_instance is not None:
            setattr(app, self.lazy_app_attribute, lazy_instance)

        @app.listener('before_server_start')
        async def mongodb_configure(app_inner, _loop):
            client_options = app_inner.config.get('MONGODB_CONNECT_OPTIONS', {})
            client = AsyncIOMotorClient(app_inner.config['MONGODB_URI'], **client_options)
            setattr(app_inner, self.app_attribute, client)

            if not hasattr(app, 'extensions'):
                setattr(app, 'extensions', {})
            app.extensions[self.extension_name] = client

            database = app_inner.config.get('MONGODB_DATABASE', None)
            if lazy_instance and database:
                motor_database_client = client[database]
                lazy_instance.init(motor_database_client)

        @app.listener('after_server_stop')
        async def mongodb_free_resources(app_inner, _loop):
            client = getattr(app_inner, self.app_attribute, None)

            if client:
                client.close()
