import os
from dotenv import load_dotenv
from autogen import ConversableAgent
from llama_index.llms.openai_like import OpenAILike

import logging


load_dotenv(".env")

print(os.getenv("OPENAI_API_BASE"))
print(os.getenv("OPENAI_API_KEY"))

text_model = "ilm2.5_2b"
vl_model = "ivl2_2b"
embed_mdoel = "bce-embedding_v1"
