import os
import time

WIN = 'nt'

# 1. file and directory need to be backup
sys = os.name
print("system type:", sys)
# use different format directory in different OS
if sys == WIN:
    source = ['C:\\ptest', 'C:\\ptest2']
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
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# zip file name
comment = input('Enter a comment -->')
# check comment enter
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# check target subdir or create it
if not os.path.exists(today):
    os.mkdir(today)
    print("Create {0} Successd".format(today))

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
