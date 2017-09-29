# my-backup-utility
The script is designed to save work managing the many sub-directories I store my backups in.

The program requires two input dirs to work:

1. 'originDir' - the source dir to backup.
2. 'backupDir' - the dir in which the backup is stored.

To go into a bit more detail:
The sub-dirs of 'originDir' and 'backupDir' are indexed, then compared.
Files with same name but different content are logged.
Files with same name and content are, obviously, skipped.
Missing sub-directories are created in 'backupDir', reflecting 'originDir'.
Files that do not have a copy under 'backupDir' are copied to their appropriate sub-directories in 'backupDir'.

