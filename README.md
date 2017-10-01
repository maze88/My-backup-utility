# my-backup-utility
The script is designed to save work managing the many sub-directories I store my backups in.

The program requires two input dirs to work, which are manually set in 'dirs.cfg':

1. 'originDir' - the source dir to backup.
2. 'backupDir' - the dir in which the backup is stored.

To go into a bit more detail:
The sub-paths of 'originDir' and 'backupDir' are indexed and then compared;

* Files that do not have a copy under 'backupDir' are copied to their appropriate sub-directories in 'backupDir'.
* Files with same name and content are skipped, as they clearly exist already in backup.
* Files with same name but different content will be logged.
* Missing and required (non-empty) sub-directories are created in 'backupDir', to reflect 'originDir'.

The folder 'initTestState' contains two folders (an origin and backup) which can be used for testing, after configuring their paths in 'dirs.cfg'.

