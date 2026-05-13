import sys
import os

# Insert the parent directory at the start of sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)  

from setup import retry_thing

@retry_thing
def test_retry_thing(name):
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    else:
        print(name, "succeeded!")
    return "Success"

print(test_retry_thing("Alice"))