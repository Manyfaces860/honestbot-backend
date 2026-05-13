from agents import Agent, OpenAIChatCompletionsModel
from constants import MODEL_NAME
from prompts import SUPPORT_ADMIRAL_SYSTEM_PROMPT
from setup import client
from tools import get_context
from schema import SupportAdmiralOutput


support_master_agent = Agent(
    name="Support_Admiral",
    instructions=SUPPORT_ADMIRAL_SYSTEM_PROMPT,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
    output_type=SupportAdmiralOutput,
)

