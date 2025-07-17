def retry(func):
    def wrapper():
        for i in range(3):
            try:
                result = func()
                return result
            except Exception as e:
                print(f"Attempt: {i + 1}, failed: {e}")
        raise Exception("All attempts failed.")
    return wrapper

@retry
def greet():
    return "Hello decorator"

print(greet())