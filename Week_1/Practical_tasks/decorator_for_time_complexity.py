def reading_file(file, chunk_size = 512):
    with open(file, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            else:
                yield chunk

import time
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Func {func.__name__} runtime: {elapsed_time:.6f} seconds")
        return result
    return wrapper


