import os
import sys
from datetime import datetime as dt
import subprocess
import re

# TODO: Make NOTES_DIR be in a config file (w/ default editor)
NOTES_DIR = '/home/hunter/Documents/notes_taking_script/notes/'

# Customizable header for new files
def header():
    return """
    ## {0} ##
    """.format(dt.today().strftime('%A %B %d, %Y'))

# Create file, add header, open file in editor
def new_note(folder='temp_notes'):
    if folder not in os.listdir(NOTES_DIR):
        os.mkdir(folder)
    folder = NOTES_DIR + folder
    os.chdir(folder)

    file_name = dt.today().strftime('%d_%b_%Y-%I:%M') + '.txt'

    f = open(file_name, 'w+')
    f.write(header())
    f.close()

    subprocess.run(['subl', file_name])
    print("Opening file: {0}".format(file_name))


# Print search match, with formatting for matching in line
def print_match(line, term):
    search = re.search(term, line)
    if search:
        for x in range(len(line)):
            if x in range(search.span()[0], search.span()[1]):
                print('v', end='')
            else:
                print(' ', end='')
        print()
        print(line)



# TODO: search is line by line, but if term goes between two lines, itll miss it
def search_files(term, folder=''):
    search_dir = NOTES_DIR + folder

    for root, dirs, files in os.walk(search_dir):
        for file in files:
            file_dir = '{0}/{1}'.format(root, file)

            # Opens every file in specified folder (or in all folders if unspecified)
            with open(file_dir) as f:
                line = f.readline()
                count = 1
                # and searches line by line for the search term
                while line:
                    if term.lower() in line.lower():
                        print("Found on line {0} of {1}".format(count, file))
                        print()
                        print_match(line, term)
                        print()
                        print("file://{0}/".format(file_dir))
                        print("-------")
                    line = f.readline()
                    count += 1

# TODO: add --help 

# Organizes the option routing and input error handling 
# os.system('tree') is used as good UI  
def main():
    for i in range(len(sys.argv)):
        arg = sys.argv[i]

        if i == 1:
            if arg == 'new':
                if len(sys.argv) <= i + 1 or sys.argv[i+1] is []:
                    new_note()
                else:
                    new_note(sys.argv[i+1])
            elif arg == 'search':
                if len(sys.argv) <= i + 1 or sys.argv[i+1:] is []:
                    print("No search term entered.")
                    os.system('tree -d {0}'.format(NOTES_DIR))
                else:
                    search_files(term=' '.join(sys.argv[i+1:]))
            elif arg == 'open':
                if len(sys.argv) <= i + 1 or sys.argv[i+1:] is []:
                    os.system('tree {0}'.format(NOTES_DIR))
                else:
                    path = '/'.join(sys.argv[i+1:])
                    print(path)
                    if os.path.isdir(NOTES_DIR + path):
                        os.system('tree {0}'.format(NOTES_DIR + path))
                    elif os.path.isfile(NOTES_DIR + path):
                        subprocess.run(['subl', NOTES_DIR + path])
                    else:
                        print("Invalid file")
                 
        # print(arg)


if __name__ == '__main__':
    main()
