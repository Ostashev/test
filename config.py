from dataclasses import dataclass

from environs import Env


@dataclass
class Settings:
    token: str
    mongo_uri: str
    db_name: str
    collection_name: str
    file_path: str


def get_config(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        token=env.str("TOKEN"),
        mongo_uri=env.str("MONGO_URI"),
        db_name=env.str("DB_NAME"),
        collection_name=env.str("COLLECTION_NAME"),
        file_path=env.str("FILE_PATH"),
    )


config = get_config('.env')
