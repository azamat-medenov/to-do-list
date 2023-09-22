from pydantic_settings import BaseSettings, SettingsConfigDict


class DBConfig(BaseSettings):
    type: str | None = None
    connector: str | None = None
    host: str | None = None
    port: int | None = None
    user: str | None = None
    password: str | None = None
    name: str | None = None
    echo: bool = False

    @property
    def db_url(self):
        return f'{self.type}+{self.connector}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'

    model_config = SettingsConfigDict(env_file='.env')


db_config = DBConfig()
