import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_core.models import ModelInfo
from autogen_ext.models.ollama import OllamaChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Define model info for gemma3
    model_info = ModelInfo(
        vision=False,
        function_calling=True,
        json_output=True,
        family="gemma"
    )
    
    ollama_client = OllamaChatCompletionClient(
        model="gemma3:4b",
        model_info=model_info,
    )

    assistant = AssistantAgent(name="assistant", model_client=ollama_client)

    await Console(assistant.run_stream(task="What is 2*4?"))
    await ollama_client.close()

asyncio.run(main())