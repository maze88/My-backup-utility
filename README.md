# My-backup-utility
script for managing my pictures backup.

The program is designed to halve my work managing pictures I collect (stored temporarily in my 'To backup' dir), by placing their backups in the correct sub-directories in my 'Backup' directory, based on the sub-directories I manually placed them in under my 'Pictures' folder.
To go into a bit more detail, the sub-dirs of my 'Pictures' dir are indexed when the script runs. Then the program scans my 'To-backup' dir (which basically contains any new pictures I collected) and checks the pictures' locations using the index, then moves them to their appropriate sub-dirs under my 'Backup' dir.

The program requires three input dirs to work:

1. new_things_dir = '~/To backup'
2. my_pic_dir = '~/Pictures'
3. backup_pic_dir = '.../Backup'

If the picture file is not found under my 'Pictures' dir, an error is printed suggesting to try manually put it in its correct sub-dir under 'Pictures'.
If the 'Backup' dir is not found, an error is printed suggeseting to check if the Flash Drive is inserted.
If the 'To backup' dir is empty, a notice is printed stating so.
