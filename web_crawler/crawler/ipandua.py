from itertools import islice
from random import choice, randint
import os


# Get the current directory of the script
current_directory = os.path.dirname(os.path.realpath(__file__))


def get_ua():
    file_path = os.path.join(current_directory, "res", "ipaddresses.txt")
    with open(file_path, "r") as uafile:
        uas = uafile.read().split("\n")
        chosen = choice(uas)
        return {'User-Agent': chosen}


def get_ip():
    # Define the relative path to the ipaddresses.txt file
    file_path = os.path.join(current_directory, "res", "ipaddresses.txt")

    # file_path = "res/ipaddresses.txt"  # Replace with your file path

    # Check if the file path exists
    if os.path.exists(file_path):
        # Check if the file itself is present
        with open(file_path, "r") as ipfile:
            ips = ipfile.read().split("\n")
            chosen = choice(ips)
            return {'http': 'http://' + chosen}




