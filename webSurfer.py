import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.agents.web_surfer import MultimodalWebSurfer
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    model_client = OpenAIChatCompletionClient(
        model="gpt-5-mini"
    )

    web_surfer_agent = MultimodalWebSurfer(
        name="WebSurfer",
        model_client=model_client,
        headless=False,
        animate_actions=True
    )

    agent_team = RoundRobinGroupChat(
        participants=[web_surfer_agent],
        max_turns=3
    )

    await Console(agent_team.run_stream(
        task="Navigate to bing and search for 'AutoGen Framework Python'. Then summarize what you find."
    ))

    await web_surfer_agent.close()
    await model_client.close()

asyncio.run(main())