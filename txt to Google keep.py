#Import a directory of utf-8 encoded text files as google keep notes.
#Text Filename is used for the title of the note.

import gkeepapi, os

username = 'username' #set to Google account user name
password = 'password' #set to Google account password

keep = gkeepapi.Keep()
success = keep.login(username,password)
dir_path = os.path.dirname(os.path.realpath(__file__))
for fn in os.listdir(dir_path):
    if os.path.isfile(fn) and fn.endswith('.txt'):
        with open(fn, 'r',encoding="utf-8") as mf:
            data=mf.read()
            keep.createNote(fn.replace('.txt',''), data)
            keep.sync()