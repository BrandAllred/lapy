#!/env/bin/env python3


import sys
import getopt
import os


SOURCE_FILE_ERR = "There was an error with the source file: "
TARGET_DIRECTORY_ERR = "There was an error with the target directory: "

def scan_directory(targetDirectory, sourceFile):
    try:
        f = open(sourceFile, "r")
        sourceFileContents = f.read()
    except OSError as err:
        print(SOURCE_FILE_ERR + str(err))
        sys.exit(2)

    try:
        print(str(os.listdir(targetDirectory)))
        #for (dirpath, dirname, filename) in os.walk(targetDirectory):
        #    print("dirpath: " + dirpath)
        #    print("dirName: " + str(dirname))
        #    print("fileName: " + str(filename))
    except OSError as err:
        print(TARGET_DIRECTORY_ERR + str(err))
        sys.exit(2)


def display_help():
    print("Options: \n" +
          "-h\tDisplays all options, and descriptions of all options.\n" +
          "-t\tTarget directory option. This tells lapy where to start. This option is required.\n" +
          "-s\tSource file option. This tells lapy what to write as the header. This option is required."
        )


def main(argv):
    try:
        optlist, args = getopt.getopt(argv, "s:t:h")
    except getopt.GetoptError as err:
        print(err)
        display_help()
        sys.exit(2)

    # Required option dictionary, so I don't have to write an if tree for each option.
    reqoptdict = {
            "-t": None,
            "-s": None,
            }

    for option in optlist:
        if option[0] in reqoptdict.keys():
            reqoptdict[option[0]] = option[1]
        elif "-h" == option[0]:
            display_help()
            return

    # Assume everything in the required option dictionary is not None.
    scan_directory(reqoptdict["-t"], reqoptdict["-s"])


main(sys.argv[1:])

