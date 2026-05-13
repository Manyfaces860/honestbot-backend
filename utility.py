from schema import SupportSessionState
from typing import List, Dict, Any

def retry_thing(func, retries=3, delay=1):
    
    def wrapper(*args, **kwargs):
        import time
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt + 1} failed with error: {e}")
                if attempt < retries - 1:
                    time.sleep(delay)
        raise Exception(f"All {retries} attempts failed.")
    
    return wrapper

def build_agent_input(
    state: SupportSessionState,
    recent_messages: List[Dict[str, str]]
) -> Dict[str, Any]:

    return {
        "state": state.model_dump(),
        "messages": recent_messages
    }

def save_state(redis_client, state: SupportSessionState):

    redis_client.set(
        state.session_id,
        state.model_dump_json()
    )

def load_state(redis_client, session_id: str) -> SupportSessionState:

    raw = redis_client.get(session_id)

    if raw:
        return SupportSessionState.model_validate_json(raw)

    return SupportSessionState(session_id=session_id)