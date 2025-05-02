try:
    with open('sample.txt', 'r') as file:
        read_file=file.read()
        print("Reading the file content:")
        print(read_file)
except Exception as e:
    print("Error :the file 'sample.txt' was not found.")