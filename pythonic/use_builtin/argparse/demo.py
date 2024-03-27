import argparse
import os


"""
Usage: python temp_file.py <operation> <args> in CMD
"""

# Create an argument parser
parser = argparse.ArgumentParser(description="CMD operations example")

# Add positional arguments
parser.add_argument("operation", choices=["echo", "mkdir", "rmdir"], help="Operation to perform")
parser.add_argument("args", nargs="*", help="Operation arguments")

# Parse the command-line arguments
args = parser.parse_args()

# Perform the corresponding operation
if args.operation == "echo":
    # Construct the command for 'echo' operation
    command = "echo " + " ".join(args.args)
elif args.operation == "mkdir":
    # Construct the command for 'mkdir' operation
    command = "mkdir " + " ".join(args.args)
elif args.operation == "rmdir":
    # Construct the command for 'rmdir' operation
    command = "rmdir " + " ".join(args.args)
else:
    # Invalid operation
    print("Invalid operation")
    exit()

# Execute the command in CMD
os.system(command)
