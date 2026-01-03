import asyncio

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Create first assistant agent
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )

    assistant = AssistantAgent(name="MathTutor",
                           model_client=openai_model_client,
                           system_message="You are helpful math tutor. Help the user solve math problems step by step"
                                          "When user says 'THANKS DONE', 'EXIT', 'THANKS' or similar, acknowledge and say 'LESSON COMPLETED' to end session."
                           )

    user_proxy = UserProxyAgent(name="Student")

    team = RoundRobinGroupChat(participants=[user_proxy, assistant],
                        termination_condition= TextMentionTermination("LESSON COMPLETED"))

    await Console(team.run_stream(task="I need help with algebra problem. Can you help me solve 2*4+5"))


asyncio.run(main())