import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    #Create first assistant agent
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )

    agent1 = AssistantAgent(
        name="MathTeacher",
        system_message="You are a math teacher. You will help the user with their math homework. Also, explain concepts clearly and ask follow-up questions",
        model_client=openai_model_client)

    agent2 = AssistantAgent(
        name="Student",
        system_message="You are a curious student. Ask questions and show your thinking process",
        model_client=openai_model_client)

    team = RoundRobinGroupChat(
        participants=[agent1, agent2],
        termination_condition=MaxMessageTermination(max_messages=6))

    await Console(team.run_stream(task="Let's discuss what is multiplication and how it works"))
    await openai_model_client.close()


asyncio.run(main())