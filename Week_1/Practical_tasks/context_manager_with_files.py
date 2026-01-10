# def read_file_in_chunks(filename, chunk_size=10):
#     with open(filename, 'r', encoding='utf-8') as file:
#         while True:
#             chunk = file.read(chunk_size)
#             if not chunk:
#                 break
#             yield chunk
#
# f = 'example.txt'
# print(read_file_in_chunks(f))

# def context_manager(file):
#     with open(file, 'r') as f:
#         while f:
#             read = f.read()
#             if not read:
#                 break
#             else:
#                 return read
#     return None
# print(context_manager('temp.txt'))

class ContextManager:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        read = open(self.file, 'r')
        self.file = read
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()