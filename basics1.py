import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    print("Hello World")

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-5-nano"
    )
    assistant = AssistantAgent(name="assistant", model_client=openai_model_client)

    await Console(assistant.run_stream(task="What is 25 * 8?"))
    await openai_model_client.close()

asyncio.run(main())