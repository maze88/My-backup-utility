import os
import shutil

def filePathsList(rootDir):
    """
    Returns a list of strings containing the paths to all the files under the parameter rootDir.
    """
    filePathsList = []
    for dirpath, dirnames, filenames in os.walk(rootDir):
        for file in filenames:
            fullPath = os.path.join(dirpath, file)
            filePathsList.append(fullPath)
    return filePathsList

def main():
    # temp dir config for testing
    originDir = '/home/maze/Documents/programming/my-backup-utility/testPicDir'
    backupDir = '/home/maze/Documents/programming/my-backup-utility/testBackupDir'

    # create lists of origin and backup dirs.
    originListing = filePathsList(originDir)
    backupListing = filePathsList(backupDir)

    print('\nRunning backup utility...')
    print('\tOrigin directory: {}\n\tOrigin directory: {}\n'.format(originDir, backupDir))
    log = []
    for filePath in originListing:
        subPath = filePath[len(originDir) + 1:]  # sub path to file within originDir.
        backupPath = os.path.join(backupDir, subPath)  # destination path in backupDir.
        if backupPath in backupListing:  # filename already exists in backup.
            if os.path.samefile(filePath, backupPath):  # file already backed up.
                pass
            else:  # different versions in origin & backup dirs.
                log.append('[-] version conflict - file with same name already exists in backup:' + subPath)
        else:  # file path doesn't yet exist.
            if os.path.exists(os.path.dirname(backupPath)):  # destination dir exists
                pass
            else:  # destination dir doesn't exist.
                subDir = os.path.dirname(subPath)
                os.mkdir(os.path.join(backupDir, subDir))
                log.append('[+] directory created in backup: ' + subDir)
            shutil.copy(filePath, backupPath)
            log.append('[+] successfully backed up: ' + subPath)

    print('Backup utility has finished running. Printing log...')
    log.sort()
    for entry in log:
        print(entry)
    print('\nExiting...')

if __name__ == '__main__':
    main()


"""
# environment setup
if configFile:
    configedDirs = read(configFile)
if configedDirs:
    print(configedDirs)
if input:
    configedDirs = input
"""
