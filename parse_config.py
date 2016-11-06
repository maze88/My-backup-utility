import ConfigParser

dir_types = ['new_things_dir', 'my_pic_dir', 'backup_pic_dir']

def get_dirs():
    config = ConfigParser.SafeConfigParser()
    config.read('dirs.cfg')
    dirs = {}
    for dir in dir_types:
        dirs[dir] = config.get('user', dir)
    return dirs


def set_dirs():
    config = ConfigParser.RawConfigParser()
    config.read('dirs.cfg')
    for dir in dir_types:
        try:
            dirs[dir] = config.get('user', dir)
        except:
            pass
    print('Configuring directories...\n"my_pic_dir" - the dir you store your pictures in.')
    print('"backup_pic_dir" - the dir you store your pictures\' backups in.')
    print('"new_things_dir" - the dir you temporarily store your new pictures in.\n')
    for blank_key in [key for key, value in dirs.items() if value == '']:
        config.set('user', blank_key, raw_input('Please enter full path of direcory for "{}" value: '.format(blank_key)))
    with open('dirs.cfg', 'wb') as cfg_file:
        config.write(cfg_file)


def main():
    if '' in get_dirs().values():
        set_dirs()
        main()
    else:
        print('Current directories configured:')
        for key, value in get_dirs().items():
            print('[+] {}: "{}"'.format(key, value))


if __name__=='__main__':
    main()
