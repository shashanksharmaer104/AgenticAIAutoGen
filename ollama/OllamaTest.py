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

    assistant = AssistantAgent(
        name="MathTutor",
        model_client=ollama_client,
        system_message="You are a expert and helpful math tutor who can solve some complex math equations and problems."
    )

    await Console(assistant.run_stream(task="Solve this linear equation. Find value of x: 4x-7(2-x)=3x+2"))
    await ollama_client.close()

asyncio.run(main())