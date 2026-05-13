from agents import Agent, OpenAIChatCompletionsModel
from constants import MODEL_NAME
from prompts import *
from setup import client
from tools import *
from schema import *


# =========================================================
# MAIN AGENT
# =========================================================

support_main_agent = Agent(
    name="MainAgent",
    instructions=MAIN_AGENT_PROMPT,
    output_type=MainAgentOutput,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# =========================================================
# SPECIALIST AGENTS
# =========================================================

returns_agent = Agent(
    name="ReturnsSpecialist",
    instructions=RETURNS_SPECIALIST_PROMPT,
    tools=[
        get_context,
        calculate_refund_amount
    ],
    output_type=SpecialistAgentOutput,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),

)


tech_agent = Agent(
    name="TechSpecialist",
    instructions=TECH_SPECIALIST_PROMPT,
    tools=[
        get_context,
        log_troubleshooting_step
    ],
    output_type=SpecialistAgentOutput,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),

)


logistics_agent = Agent(
    name="LogisticsSpecialist",
    instructions=LOGISTICS_SPECIALIST_PROMPT,
    tools=[
        get_context,
        check_customs_status
    ],
    output_type=SpecialistAgentOutput,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),

)


security_agent = Agent(
    name="SecuritySpecialist",
    instructions=SECURITY_SPECIALIST_PROMPT,
    tools=[
        get_context,
    ],
    output_type=SpecialistAgentOutput,
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),

)

def human_handoff_handle():
    pass

def fallback():
    pass