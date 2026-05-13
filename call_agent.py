from agents import Runner
from setup import *
from logger import logger, logging
from agent import support_main_agent
from utility import load_state, save_state, build_agent_input
import asyncio

async def agent_loop(query):
    
    # prepare user input to give query and session context to the agent
    
    
    # run agent with query and session
    
    
    # route based on the main agent's output, for example if the main agent determines the query is about returns, route to the returns specialist agent and give it the same query and session context. You can also give it tools to use that are relevant to the specialist agent's domain.
    
    
    # based on specialist agent output, either return final response to user or escalate to human support if needed.
    result = await Runner.run(support_main_agent, input=query, session=session)
    logger.log(level=logging.INFO, msg=f"final output: {result.final_output.response}")
    return result.final_output.response

if __name__ == "__main__":
    asyncio.run(agent_loop('I bought an AuraPulse Pro last week and I want to return it. Can I?'))