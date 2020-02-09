# Normal Header Adder

import os
import sys

SOURCE_FILE_ERR = "There was an error with the source file: "
TARGET_DIRECTORY_ERR = "There was an error with the target directory: "


class Nhapy:
    """
        Normal Header Adder Python
        This routine runs synchronously.
    """

    def insert_headers(self, target_directory, source_file):
        try:
            file = open(source_file, "r")
            file_contents = file.read()
            print("file contents: " + file_contents)
        except OSError as err:
            print(SOURCE_FILE_ERR + str(err))
            sys.exit(2)

        if sys.platform == "win32":
            file_path_delimiter = "\\"
        else:
            file_path_delimiter = "/"

        # Get all of the files, so we can count and iterate through all of the files.
        target_files = []

        targets = os.listdir(target_directory)
        for place in targets:
            # If we fail to add a file, keep picking up files that we can add things to, and report the ones that we
            # can't
            try:
                if os.path.isfile(target_directory + file_path_delimiter + place):
                    target_files += [file_path_delimiter + place]
                else:
                    # Not a good solution, but it works as a first iteration.
                    # TODO: make this portion more efficient
                    new_targets = os.listdir(target_directory + file_path_delimiter + place)
                    for new_place in new_targets:
                        targets += [place + file_path_delimiter + new_place]
            except OSError as err:
                print(TARGET_DIRECTORY_ERR + str(err))
                sys.exit(2)

        # TODO: make this do more than just say that it's a file.
        for file in target_files:
            if os.path.isfile(target_directory + file):
                print(file + " is a file!")
            else:
                print(file + " isn't a file.")

