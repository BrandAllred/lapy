#!/env/bin/env python3

import sys
import getopt
import nhapy


def object_factory(option_list):
    """For now, we only need to return one type of object"""
    return nhapy.Nhapy()


def display_help():
    print("Options:\n" +
          "-h\tDisplays all options, and descriptions of all options.\n" +
          "\nArguments:\n" +
          "First argument:\t\tThis tells lapy where to start. Include double quotes if the file location has a space " +
          "in it.\n" +
          "Second argument:\tThis tells lapy what to write as the header.\n" +
          "\nAll arguments are required!"
          )


def main(argv):
    try:
        option_list, argument_list = getopt.getopt(argv, "h")
    except getopt.GetoptError as err:
        print(err)
        display_help()
        sys.exit(2)

    for option in option_list:
        if "-h" == option[0]:
            display_help()
            return

    try:
        target_directory = argument_list[0]
        source_file = argument_list[1]

        header_handler = object_factory(option_list)

        header_handler.insert_headers(target_directory, source_file)
    except IndexError:
        print("\nERROR: An argument was missing.\n")
        display_help()
        sys.exit(2)


main(sys.argv[1:])
