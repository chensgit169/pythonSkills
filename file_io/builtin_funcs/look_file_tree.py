import os


def print_directory_contents(path):
    # iterate over all the files and folders in the given path
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


def demo():
    # specify the path of the directory to view
    directory_path = os.getcwd()

    # call the function to view all the folders and files in the directory
    print_directory_contents(directory_path)


if __name__ == '__main__':
    demo()
