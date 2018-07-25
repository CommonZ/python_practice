import os
import time

WIN = 'nt'

# 1. file and directory need to be backup
sys = os.name
print("system type:", sys)
# use different format directory in different OS
if sys == WIN:
    source = ['"C:\\ptest"']
else:
    source = ['/Users/fzhu/notes']

# 2. save directory
# Linux & Mac OS
# Windows
if sys == WIN:
    target_dir = 'D:\\Backup'
else:
    target_dir = '/Users/fzhu/backup'

# 3. package file to zip
# 4. filename by date and time
target = target_dir + os.sep + \
         time.strftime('%Y%m%d_%H%M%S') + '.zip'

# check target dir or create it
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. use zip package it
if sys == WIN:
    # please install 7-zip, and add software directory to Windows PATH
    zip_command = '7z a {0} {1}'.format(target, ' '.join(source))
else:
    zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# run backup
print('Zip command is:', zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('Back up successed to', target)
else:
    print('Backup failed!')
