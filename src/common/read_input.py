from _typeshed import FileDescriptorOrPath


def read_input(file_path: FileDescriptorOrPath) -> str:
    with open(file_path, "r") as file:
        return file.read()
