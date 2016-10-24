import hashlib, sys, os, shutil, config_parser

def main():
    #reading configuration file to get user defined dirs.
    dirs=config_parser.get_dirs()
    new_things_dir=dirs['new_things_dir']
    my_pic_dir=dirs['my_pic_dir']
    backup_pic_dir=dirs['backup_pic_dir']

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

    #generate index dictionary where hashhex(file)=key and path(file)=value. 
    print('Generating hash index of picture dir, this could take several minutes depending on its size...')
    path_hash={}
    for root, dirs, files in os.walk(unicode(my_pic_dir)):
        for file in files:
            path_hash[hashhex(os.path.join(root,file))]=os.path.join(root,file)
    print('[+] File index complete!\n')

    #backup process:
    print('Moving all files from: "%s" to their appropriate subdirectories under: "%s" (subdirectories\' paths based on paths from "%s")...' % (new_things_dir,backup_pic_dir,my_pic_dir))
    report=['Done!\n\nPrinting report:']
    for file in os.listdir(unicode(new_things_dir)):
        if hashhex(os.path.join(new_things_dir,file)) in path_hash:
            src=os.path.join(new_things_dir,file)
            des=os.path.join(backup_pic_dir+path_hash[hashhex(os.path.join(new_things_dir,file))][len(my_pic_dir):])
            try:
		shutil.move(src,des)
		report.append('[+] file backed up: %s' % file)
	    except IOError:
		report.append('[-] ERROR: No such directory %s.' % des)
        else:
            report.append('[-] ERROR: Not yet placed in pic library: %s' % file)

    #print report.
    if len(report)>1:
	for entry in report:
	    print(entry)
    else:
	print('[-] ERROR: No files to backup found in %s.' % new_things_dir)
    print('\nBack utility has finished running.\n')

if __name__=='__main__':
    main()

