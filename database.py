from motor.motor_asyncio import AsyncIOMotorClient

from config import config


async def connect_to_mongo():
    client = AsyncIOMotorClient(config.mongo_uri)
    return client[config.db_name][config.collection_name]
