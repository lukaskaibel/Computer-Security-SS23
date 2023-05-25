import os


def read_all_files_in_directory(directory, file_extension):
    file_contents = []
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            with open(os.path.join(directory, filename), "r") as f:
                content = f.read()
                if all(ord(c) < 128 for c in content):
                    ascii_content = content.encode("ascii")
                    file_contents.append(ascii_content)
                else:
                    raise ValueError("Non-ASCII characters found in the input file.")
    return file_contents
