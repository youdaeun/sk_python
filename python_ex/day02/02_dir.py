import os

search_dir = "D:\\python_ex\\day02\\"
for curdir, dirs, files in os.walk(search_dir):
    print(f'{curdir} - {dirs} - {files}')
#curdir  D:\python_ex\day02\ - ['static', 'upload'] - ['01.py', '01_dir.py', '02.py', '02.txt', '02_dir.py', '03.php', 'test.txt']
#dirs D:\python_ex\day02\static - [] - ['static_01.py', 'static_02.txt']
#files D:\python_ex\day02\ - ['static', 'upload'] - ['01.py', '01_dir.py', '02.py', '02.txt', '02_dir.py', '03.php', 'test.txt']
#      D:\python_ex\day02\static - [] - ['static_01.py', 'static_02.txt']
#      D:\python_ex\day02\upload - [] - []