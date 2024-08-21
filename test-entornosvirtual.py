import os

def find_virtualenvs(root_folder="~"):
    root_folder = os.path.expanduser(root_folder)
    for root, dirs, files in os.walk(root_folder):
        if 'bin' in dirs and 'activate' in os.listdir(os.path.join(root, 'bin')):
            print(f"Found virtualenv: {root}")

find_virtualenvs()