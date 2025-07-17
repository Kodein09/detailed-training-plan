def read_file_in_chunks(filename, chunk_size=10):
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

f = 'example.txt'
print(read_file_in_chunks(f))