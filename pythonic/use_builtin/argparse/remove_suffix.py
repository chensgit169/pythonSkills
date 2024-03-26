import os
import argparse


def remove_suffix(folder_path, suffix):
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):

        # Construct the old and new file paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, filename.rsplit(suffix, 1)[0])

        # Rename the file by removing the suffix
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Batch rename files in a folder by removing a specified suffix")
    parser.add_argument("suffix", help="Suffix to remove from filenames")
    parser.add_argument("-f", "--folder_path", help="Path to the folder containing files to rename. "
                                                    "Defaults to current directory", default=os.getcwd())
    args = parser.parse_args()

    # Validate folder path
    if not os.path.isdir(args.folder_path):
        print("Error: Invalid folder path")
        exit()

    # Perform batch renaming
    remove_suffix(args.folder_path, args.suffix)