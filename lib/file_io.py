def write_file(file_name, file_content):
    
    with open("file_name.txt", mode ="w",encoding="utf-8") as file_name:
       return file_name.write(file_content)
def append_file(file_name, append_content):
    with open("file_name.txt", mode="w", encoding="utf-8") as file_name:
        return file_name.write(append_content)

def read_file(file_name):
    with open("file_name.txt", encoding="utf-8") as file_name:
        for line in file_name:
            return(line)


# use write_file function. 
print(write_file(file_name="logfile", file_content="Log 1: 5 bananas added" ))
print(append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted"))

print (read_file(file_name="logfile"))
# Log 1: 5 bananas added
# Log 2: 3 bananas subtracted