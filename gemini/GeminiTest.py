import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    gemini_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash"
    )

    assistant = AssistantAgent(name="assistant", model_client=gemini_client)

    await Console(assistant.run_stream(task="What is the capital of France?"))
    await gemini_client.close()


asyncio.run(main())