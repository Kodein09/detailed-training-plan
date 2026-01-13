# def read_big_file(file, chunk_size = 1024):
#     with open(file, "r") as f:
#         while True:
#             chunk = f.read(chunk_size)
#             if not chunk:
#                 break
#             else:
#                 yield chunk
#
# for chunk in read_big_file("car_sales_data.csv", 256):
#     print(chunk)

# def reading_chunks_via_generator(file, chunk_size=2):
#     with open(file) as f:
#         while True:
#             chunk = f.read(chunk_size)
#             if not chunk:
#                 break
#             else:
#                 yield chunk
#
# for chunk in read_big_file("car_sales_data.csv", 256):
#     print(chunk)
#
# gen = reading_chunks_via_generator('temp.txt')
# for chunk in gen:
#     print(chunk)

def read_chunks(file, chunk_size=32):
    with open(file) as f:
        while f:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            else:
                yield chunk

for chunk in read_chunks('temp.txt'):
    print(chunk)