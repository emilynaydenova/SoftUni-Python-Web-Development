import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
output_file_path = BASE_DIR / 'report.txt'

# all files in current directory + first level files in subdirectories
directory_files = []
# files by extensions
found_files = {}

for element in os.listdir(BASE_DIR):  # Return a list containing the names of the files in the directory.
    if os.path.isdir(BASE_DIR / element):
        sub_directory = BASE_DIR / element
        for f in os.listdir(sub_directory):
            if os.path.isfile(sub_directory / f):
                directory_files.append(f)
    else:
        directory_files.append(element)
 

for element in directory_files:
    if os.path.isfile(element):
        extension = '' if (element.find('.') == -1) else element.split('.')[-1]
        if extension not in found_files:
            found_files[extension] = []
        found_files[extension].append(element)

# sort by file names
for value in found_files.values():
    value.sort()
# sort by file extensions
found_files = dict(sorted(found_files.items()))

with open(output_file_path, 'w') as report:
    report.write(f'Directory Traversal of {BASE_DIR}:\n')

    for extension, file_names in found_files.items():
        print(f'.{extension}', file=report)
        [print(f'- - - {file_name}', file=report) for file_name in file_names]
