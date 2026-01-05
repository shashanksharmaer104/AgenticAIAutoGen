import asyncio
import os

from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
from dotenv import load_dotenv

load_dotenv()

async def async_value_stream(value):
    yield value

async def main():
    mini_model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )

    main_model_client = OpenAIChatCompletionClient(
        model="gpt-5"
    )

    value = os.getenv("JIRA_USERNAME")

    await Console(async_value_stream(value))

    StdioServerParams(
        command="uvx",
        args=["mcp-atlassian"]
    )




asyncio.run(main())