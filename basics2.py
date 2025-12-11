import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    print("Hello World")

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )
    assistant = AssistantAgent(name="file_processing_assistant", model_client=openai_model_client)

    image = Image.from_file("/Users/shashanksharma/PycharmProjects/AgenticAIAutoGen/images/sample_image.jpg")
    multimodel_message = MultiModalMessage(
        content=["What do you see in this image?", image],
        source="user"
    )

    await Console(assistant.run_stream(task=multimodel_message))
    await openai_model_client.close()

asyncio.run(main())