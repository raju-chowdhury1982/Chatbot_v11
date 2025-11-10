################ import and testing code script ################

# import os
# import sys
# # the root directory to Python path to run the script directly
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# # for testing run as :python -m app.graph.tools.aoai_chat

###############################################################################

from app.settings import settings
from openai import AzureOpenAI

_client = AzureOpenAI(
    api_key=settings.aoai_api_key,
    api_version=settings.aoai_api_version,
    azure_endpoint=settings.aoai_endpoint,
)


async def chat_prompt(messages, temperature: float = 0.0, max_tokens: int = 1000):  # type: ignore
    resp = _client.chat.completions.create(
        model=settings.aoai_chat_deployment,
        messages=messages,  # type: ignore
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content


async def embed(text: str):
    resp = _client.embeddings.create(
        model=settings.aoai_embed_deployment,
        input=text,
    )
    return resp.data[0].embedding
