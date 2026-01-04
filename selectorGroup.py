import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Create model client
    model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )

    researcher = AssistantAgent(
        name="ResearcherAgent",
        model_client=model_client,
        system_message="You are a researcher. Your role is to gather information and provide research findings. "
                       "Do not write articles or create account - just provide research date and facts."
    )

    writer = AssistantAgent(
        name="WriterAgent",
        model_client=model_client,
        system_message="You are a writer. Your role is to take research information and create well-written short articles. "
                       "Wait for reacher to be provided, then write the content."
    )

    critic = AssistantAgent(
        name="CriticAgent",
        model_client=model_client,
        system_message="You are a critic. Review written content and provide feedback. Provide rating/stars on a scale of 1 to 5."
                       "Say 'TERMINATE' when satisfied with the final result."
    )

    text_termination = TextMentionTermination("TERMINATE")
    max_msg_termination = MaxMessageTermination(max_messages=15)

    termination = text_termination | max_msg_termination

    team = SelectorGroupChat(
        participants=[critic, writer, researcher],
        model_client=model_client,
        termination_condition=termination,
        allow_repeated_speaker=True
    )

    await Console(team.run_stream(task="Research about use of AI with agents in Quality Engineering (Automation testing) trend and write a brief article about the future and it's impact on Software testing around the world"))


asyncio.run(main())