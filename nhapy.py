# Normal Header Adder

import os
import sys

SOURCE_FILE_ERR = "There was an error with the source file: "
TARGET_DIRECTORY_ERR = "There was an error with the target directory: "


class Nhapy:
    def insert_headers(self, target_directory, source_file):
        try:
            file = open(source_file, "r")
            file_contents = file.read()
            print("file contents: " + file_contents)
        except OSError as err:
            print(SOURCE_FILE_ERR + str(err))
            sys.exit(2)

        try:
            print(str(os.listdir(target_directory)))
        except OSError as err:
            print(TARGET_DIRECTORY_ERR + str(err))
            sys.exit(2)

