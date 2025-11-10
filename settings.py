# Store all the enviornmental variables here
# pyright: reportUnknownVariableType=false

import os  # type: ignore

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)

from typing import Optional  # type: ignore

from pydantic import ConfigDict, Field  # type: ignore
from pydantic_settings import BaseSettings


class Settings(BaseSettings):  # type: ignore
    # Azure OpenAI
    aoai_endpoint: str = os.getenv("AZURE_OPENAI_ENDPOINT")  # type: ignore
    aoai_api_key: str = os.getenv("AZURE_OPENAI_API_KEY")  # type: ignore
    aoai_api_version: str = "2024-02-15-preview"  # type: ignore
    aoai_chat_deployment: str = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")  # type: ignore
    aoai_embed_deployment: str = os.getenv("AZURE_OPENAI_EMBED_DEPLOYMENT")  # type: ignore

    # Azure Search
    search_endpoint: str = os.getenv("AZURE_SEARCH_ENDPOINT")  # type: ignore
    search_api_key: str = os.getenv("AZURE_SEARCH_API_KEY")  # type: ignore
    search_index: str = os.getenv("AZURE_SEARCH_INDEX_NAME")  # type: ignore
    search_embed_field: str = Field(default="content_vector", json_schema_extra="AZURE_SEARCH_EMBED_FIELD")  # type: ignore

    # App
    app_log_level: str = Field(default="INFO", json_schema_extra="APP_LOG_LEVEL")  # type: ignore
    allow_origins: str = Field(default="*", json_schema_extra="ALLOW_ORIGINS")  # type: ignore

    model_config = ConfigDict(  # type: ignore
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )  # type: ignore


try:
    settings = Settings()  # type: ignore
except Exception as e:
    print(f"Error loading settings: {e}")
    raise e


# ======== for current file debugging purposes only

# if __name__ == "__main__":
#     print("Running settings directly")
#     # for debugging purposes
#     print(settings.search_index)

# =====================================
