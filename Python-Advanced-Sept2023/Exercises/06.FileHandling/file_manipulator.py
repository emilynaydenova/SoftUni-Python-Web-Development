import os


def create_file(*value):
    file_name = value[0]
    open(file_name, 'w').close()
    return "File is created"


def add_content(*value):
    file_name, content = value
    if os.path.exists(file_name) and content:
        with open(file_name, 'a') as f:
            f.write(content + '\n')
            return "Added content"


def replace_content(*value):
    file_name, old_string, new_string = value
    if os.path.exists(file_name):
        with open(file_name, 'r+') as f:
            content = f.read()
            new_content = content.replace(old_string, new_string)
            f.seek(0)
            f.write(new_content)
            return "Content is replaced"

    return "An error occurred"


def delete_file(*value):
    file_name = value[0]
    if os.path.exists(file_name):
        os.remove(file_name)
        return "File is deleted"
    else:
        return 'An error occurred'


commands = {'Create': create_file,
            'Add': add_content,
            'Replace': replace_content,
            'Delete': delete_file
            }

while (line := input()) != 'End':
    command, *args = line.split('-')
    if command in commands:
        log = commands.get(command)(*args)
        print(log)
    else:
        print('No such command')
print('End')

"""
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
error-file.txt
Delete-random.txt
Delete-file.txt
End

"""
