import sys
import os
import shutil
import hashlib

import parse_config # local module


def hashhex(filepath):
    ```Returns the hash of a file <filepath> in hex format.```

    blocksize = 2**10
    hasher = hashlib.md5()
    with open(filepath, 'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    return hasher.hexdigest()


def index_pics(dir):
    ```Generates a dictionary of the designated my_pic_dir,
    using the hashhex(filepath) result as the key, and the filepath as the value.
    ```

    dir_hash = {}
    for root, dirs, files in os.walk(unicode(dir)):
        for file in files:
            dir_hash[hashhex(os.path.join(root, file))] = os.path.join(root, file)
    print('[+] File index complete!\n')
    return dir_hash


def main():
    dirs = config_parser.get_dirs()
    new_things_dir = dirs['new_things_dir']
    my_pic_dir = dirs['my_pic_dir']
    backup_pic_dir = dirs['backup_pic_dir']

    print('Generating hash index of picture dir, this could take several minutes depending on its size...')
    path_hash = index_pics(my_pic_dir)

    print('Moving all files from: "{}" to their appropriate subdirectories under: "{}" (subdirectories\' paths based on paths from "{}")...'.format(new_things_dir, backup_pic_dir, my_pic_dir))
    report = []  # prepared for logging results
    for file in os.listdir(unicode(new_things_dir)):
        if hashhex(os.path.join(new_things_dir, file)) in path_hash:
            src = os.path.join(new_things_dir, file)
            des = os.path.join(backup_pic_dir+path_hash[hashhex(os.path.join(new_things_dir, file))][len(my_pic_dir):])
            try:
                shutil.move(src, des)
                report.append('[+] file backed up: {}'.format(file))
            except IOError:
                report.append('[-] ERROR: No such directory {}.'.format(des))
        else:
            report.append('[-] ERROR: Not yet placed in pic library: {}'.format(file))

    if report:
        print('Done!\n\nPrinting report:')
        for entry in report:
            print(entry)
    else:
        print('[-] ERROR: No files to backup found in {}.'.format(new_things_dir))

    print('\nBack utility has finished running.\n')


if __name__=='__main__':
    main()
