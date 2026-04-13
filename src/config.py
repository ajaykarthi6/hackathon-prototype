from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Interstellar Agent ADK"
    environment: str = "development"
    port: int = 8000


settings = Settings()
