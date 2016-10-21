 -*- coding: utf8 -*-

import hashlib, sys, os, shutil

new_things_dir='C:\Users\Maze\Desktop\To backup'
my_pic_dir='C:\Users\Maze\Pictures'
backup_pic_dir='F:\BACKUP_0526840900\Pictures'
my_stuff_dir='C:\STUFF'
backup_stuff_dir='F:\BACKUP_0526840900\Stuff'

def main():
    #return hash of file bytes.
    def hashhex(filepath):
        blocksize=2**10
        hasher=hashlib.md5()
        with open(filepath, 'rb') as afile:
            buf=afile.read(blocksize)
            while len(buf)>0:
                hasher.update(buf)
                buf=afile.read(blocksize)
        return hasher.hexdigest()

    #generate dictionary where hash(file)=key and path(file)=value. 
    path_hash={}
    for root, dirs, files in os.walk(unicode(my_pic_dir)):
        for file in files:
            path_hash[hashhex(os.path.join(root,file))]=os.path.join(root,file)

    #describe forthcoming action.
    print('\nRunning backup utility:')
    print('moving all files from: "%s" to their appropriate subdirectories under: "%s" (subdirectories\' paths based on paths from "%s")' % (new_things_dir,backup_pic_dir,my_pic_dir))

    #take action.
    report=['done.\n\nprinting report:']
    for file in os.listdir(unicode(new_things_dir)):
        if hashhex(os.path.join(new_things_dir,file)) in path_hash:
            src=os.path.join(new_things_dir,file)
            des=os.path.join(backup_pic_dir+path_hash[hashhex(os.path.join(new_things_dir,file))][len(my_pic_dir):])
            try:
		shutil.move(src,des)
        	report.append('[+] file backed up: %s' % file)
	    except IOError:
		report.append('[-] ERROR: no such directory %s.' % des)
        else:
            report.append('[-] ERROR: not yet placed in pic library: %s' % file)

    #print report.
    if len(report)>1:
	for entry in report:
	    print(entry)
    else:
	print('[-] ERROR: no files to backup found in %s' % new_things_dir)
    print('\nback utility has finished running.')

if __name__=='__main__':
    main()
