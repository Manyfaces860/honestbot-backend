
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