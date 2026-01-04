import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Setup MCP server
    filesystem_server_params = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/Users/shashanksharma/PycharmProjects/AgenticAIAutoGen"
        ],
        read_timeout_seconds=60
    )

    # Start MCP server
    fs_workbench = McpWorkbench(filesystem_server_params)

    async with fs_workbench as fs_wb:
        # Create model client
        openai_model_client = OpenAIChatCompletionClient(
            model="gpt-5-mini"
        )

        assistant = AssistantAgent(
            name="MathTutor",
            model_client=openai_model_client,
            workbench=fs_wb,
            system_message="You are helpful math tutor. Help the user solve math problems step by step. "
                           "You have access to file system. "
                           "When user says 'THANKS DONE', 'EXIT', 'THANKS' or similar, acknowledge and say 'LESSON COMPLETED' to end session."
        )

    user_proxy = UserProxyAgent(name="Student")

    team = RoundRobinGroupChat(participants=[user_proxy, assistant],
                        termination_condition= TextMentionTermination("LESSON COMPLETED"))

    await Console(team.run_stream(task="I need help with algebra problems. "
                                       "Tutor, feel free to create files to help the student learning."))


asyncio.run(main())