#!/usr/bin/env python3.7

import os

user_path = input("Enter the path: ")


if os.path.exists(user_path):

    fd_list = os.listdir(user_path)

    for each in fd_list:

        full_path = os.path.join(user_path,each)

        if os.path.exists(full_path) and os.path.isdir(full_path):
            print(f"{each} \t\t\t\t is a directory")
        elif os.path.exists(full_path) and os.path.isfile(full_path):
            print(f"{each} \t\t\t\t is file")

else:
    print("path does not exists")



