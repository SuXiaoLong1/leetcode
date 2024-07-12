# Function to write data to a file
def write_data(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

# Function to read data from a file
def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

# Example usage
if __name__ == "__main__":
    file_name = "example.txt"
    data = "Hello, PyCharm!"
    write_data(file_name, data)
    print(read_data(file_name))
    print(1)