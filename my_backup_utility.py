import filecmp
import os
import shutil

def filePathsList(rootDir):
    """
    Returns a list of strings containing the paths to all the files under the parameter 'rootDir'.
    """
    filePathsList = []
    for dirpath, dirnames, filenames in os.walk(rootDir):
        for file in filenames:
            fullPath = os.path.join(dirpath, file)
            filePathsList.append(fullPath)
    return filePathsList

def setDirs():  # incomplete docstring & functionality
    """
    Set origin and backup dirs here for utility to use:
    """
    originDir = '/home/maze/Pictures'
    backupDir = '/media/maze/Samsung USB/Pictures'

    if not os.path.exists(originDir) or not os.path.exists(backupDir):
        print('[-] ' + 'Specifified origin and/or backup directory do not exist.\nExiting...')
        exit()
    else:
        print('\tOrigin directory: {}\n\tBackup directory: {}\n'.format(originDir, backupDir))
        return (originDir, backupDir)

def printSortedLines(array, precursor=''):
    """
    Sorts and prints all elements from an array. Returns the length
    of the array.
    Takes the optional parameter 'precursor', which it prints before
    each element.
    """
    lineCount = len(array)
    if lineCount:
        array.sort()
        for line in array:
            print(precursor + line)
    return lineCount

def main():
    print('Running backup utility...\n')

    goodIcon = '[+] '
    badIcon = '[-] '
    eventsLog = []
    originDir, backupDir = setDirs()
    originListing = filePathsList(originDir)
    backupListing = filePathsList(backupDir)

    # main logic block
    for filePath in originListing:
        subPath = filePath[len(originDir) + 1:]  # sub path to file within originDir.
        backupPath = os.path.join(backupDir, subPath)
        if backupPath in backupListing and not filecmp.cmp(filePath, backupPath):
            eventsLog.append(badIcon + 'File with same name already exists in backup:' + subPath)
        else:
            if not os.path.exists(os.path.dirname(backupPath)):
                subDir = os.path.dirname(subPath)
                os.mkdir(os.path.join(backupDir, subDir))
                eventsLog.append(goodIcon + 'Directory created in backup: ' + subDir)
            shutil.copy(filePath, backupPath)
            eventsLog.append(goodIcon + 'Backed up: ' + subPath)

    # finishing up
    print('Backup utility has finished running. Printing log:\n')
    if not printSortedLines(eventsLog, '\t'):
        print('\t' + goodIcon + 'All file backups up to date.')
    print('\nExiting...')

if __name__ == '__main__':
    main()

