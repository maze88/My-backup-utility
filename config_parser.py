import ConfigParser

def get_dirs():
    config=ConfigParser.RawConfigParser()
    config.read('dirs.cfg')
    dirs={'new_things_dir':config.get('user','new_things_dir'),
          'my_pic_dir':config.get('user','my_pic_dir'),
          'backup_pic_dir':config.get('user','backup_pic_dir')
	 }
    if '' in dirs.values():
	set_dirs()
	get_dirs()

    return dirs

def set_dirs():
    pass
    #this function should prompt the user for empty values and write them to the config file.
    #if this user inserts an empty value, do not write - leave the current value in the config file.

def main():
    print('Current directories configured:')
    for key, value in get_dirs().items():
        print('[+] %s: "%s"' % (key,value))

if __name__=='__main__':
    main()

