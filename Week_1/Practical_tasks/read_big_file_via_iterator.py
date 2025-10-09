def read_big_file(file, chunk_size = 1024):
    with open(file, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            else:
                yield chunk

for chunk in read_big_file("car_sales_data.csv", 256):
    print(chunk)