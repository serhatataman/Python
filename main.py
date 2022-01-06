# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

if __name__ == '__main__':
    if not os.path.exists("/content/drive/MyDrive/ProjectAmbition/stylegan3/dataset_tool.py"):
        raise FileNotFoundError("dataset_tool.py file does not exist!")

    if os.path.exists("/content/drive/MyDrive/ProjectAmbition/raw_data"):
        raise FileNotFoundError("raw_data folder does not exist!")

    if os.path.exists("/content/drive/MyDrive/ProjectAmbition/datasets"):
        raise FileNotFoundError("datasets folder does not exist!")