import asyncio
import json

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
        name="HelperAgent",
        #system_message="You are a math teacher. You will help the user with their math homework. Also, explain concepts clearly and ask follow-up questions",
        model_client=openai_model_client)

    agent2 = AssistantAgent(
        name="BackupHelperAgent",
        #system_message="You are a curious student. Ask questions and show your thinking process",
        model_client=openai_model_client)

    # team = RoundRobinGroupChat(
    #     participants=[agent1, agent2],
    #     termination_condition=MaxMessageTermination(max_messages=6))

    await Console(agent1.run_stream(task="My favourite color is Blue."))
    state = await agent1.save_state()
    with open("memory.json", "w") as f:
        json.dump(state, f, default=str)

    with open("memory.json", "r") as f:
        saved_state = json.load(f)

    await agent2.load_state(saved_state)
    await Console(agent2.run_stream(task="What is my favorite color?"))

    await openai_model_client.close()


asyncio.run(main())