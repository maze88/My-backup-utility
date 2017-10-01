import filecmp
import os
import re
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

def getSetting(settingsFile, settingTitle):
    """
    Reads 'settingsFile' and finds the last instance of 'settingTitle'. Returns the
    value of 'settingTitle' that comes after te '=' sign, removing any trailing whitespaces
    and any closing '/' or '\'.
    If not found, returns False.
    """
    setting = False
    with open(settingsFile, 'r') as settings:
        for line in settings:
            settingRegexp = re.search(settingTitle + '\s*=\s*(.+)', line)
            if settingRegexp:
                setting = settingRegexp.group(1).strip().rstrip('/').rstrip('\\')

    re.purge()
    return setting

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

    # initiation block
    goodIcon = '[+] '
    badIcon = '[-] '
    eventsLog = []
    originDir = getSetting('dirs.cfg', 'originDir')
    backupDir = getSetting('dirs.cfg', 'backupDir')
    print('\tOrigin directory: {}\n\tBackup directory: {}\n'.format(originDir, backupDir))
    if not os.path.exists(originDir) or not os.path.exists(backupDir):
        print('[-] ' + 'Specifified origin and/or backup directory do not exist.\nExiting...')
        exit()
    originListing = filePathsList(originDir)
    backupListing = filePathsList(backupDir)

    # main logic block
    for filePath in originListing:
        subPath = filePath[len(originDir) + 1:]  # sub-dir path to file
        subDir = os.path.dirname(subPath)
        backupPath = os.path.join(backupDir, subPath)
        if backupPath in backupListing:
            sameFile = filecmp.cmp(filePath, backupPath, False)
            if not sameFile:
                eventsLog.append(badIcon + 'Different file with same name already exists in backup:' + subPath)
        else:
            if not os.path.exists(os.path.join(backupDir, subDir)):
                os.mkdir(os.path.join(backupDir, subDir))
                eventsLog.append(goodIcon + 'Directory created in backup: ' + subDir)
            shutil.copy(filePath, backupPath)
            eventsLog.append(goodIcon + 'Backed up: ' + subPath)

    # termination block
    print('Backup utility has finished running. Printing log:\n')
    if not printSortedLines(eventsLog, '\t'):
        print('\t' + goodIcon + 'All file backups up to date.')
    print('\nExiting...')

if __name__ == '__main__':
    main()

