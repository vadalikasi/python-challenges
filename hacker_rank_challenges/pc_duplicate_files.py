import os
import pandas as pd


def list_file_names(file_dir_name):
    path=file_dir_name
    for i in file_dir_name:
        if os.path.isdir(i):
            list_file_names(os.listdir(i))
        else:
            yield i


if __name__ == "__main__":
    # get drive for which you want to identify files which are duplicates
    drive_name = "C:"
    list_file_names(drive_name)
    print(list(list_file_names(os.listdir(drive_name))))

