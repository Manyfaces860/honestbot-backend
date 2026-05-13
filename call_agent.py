from agents import Runner
from setup import *
from logger import logger, logging
from agent import support_master_agent
import asyncio

async def call_agent(query):
    result = await Runner.run(support_master_agent, input=query, session=session)
    logger.log(level=logging.INFO, msg=f"final output: {result.final_output.response}")
    return result.final_output.response

if __name__ == "__main__":
    asyncio.run(call_agent('I bought an AuraPulse Pro last week and I want to return it. Can I?'))