# My-backup-utility
script for managing my pictures backup.

The program is designed to halve my work managing pictures I collect (stored temporarily in my 'To backup' dir), by placing their backups in the correct sub-directories in my 'Backup' directory, based on the sub-directories I manually cpoied them to under my 'Pictures' folder.

To go into a bit more detail, the sub-dirs of my 'Pictures' dir are indexed by the script runs. Then the program scans my 'To-backup' dir (which basically contains any new pictures I collected) and checks those pictures' locations are under my 'Picture' dir using the index, then moves them to their appropriate sub-dirs under my 'Backup' dir, deleting the copy in the 'To backup' dir.

The program requires three input dirs to work:

1. 'my_pic_dir' - the dir you store your pictures in.
2. 'backup_pic_dir' - the dir you store your pictures' backups in.
3. 'new_things_dir' - the dir you temporarily store your new pictures in.

If the picture file is not found under my 'Pictures' dir, an error is printed suggesting that the user still hasn't copied it to an appropriate sub-dir under 'Pictures'.
If the 'Backup' dir is not found, an error is printed suggeseting to check if the Flash Drive is inserted.
If the 'To backup' dir is empty, a notice is printed stating so.
