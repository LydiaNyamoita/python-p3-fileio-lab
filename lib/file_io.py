def write_file(file_name, file_content):
    
    with open("file_name.txt", mode ="w",encoding="utf-8") as file_name:
        file_name.write(file_content)
def append_file(file_name, append_content):
    with open("file_name.txt", mode="w", encoding="utf-8") as file_name:
        file_name.write(append_content)

def read_file(file_name):
    with open("file_name.txt", encoding="utf-8") as file_name:
        for line in file_name:
            print(line)
