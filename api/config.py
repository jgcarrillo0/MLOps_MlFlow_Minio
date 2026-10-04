from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mlflow_tracking_uri: str = "http://mlflow:5000"
    mlflow_model_name: str = "covertype_classifier"
    mlflow_model_alias: str = "champion"

    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
