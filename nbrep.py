from os.path import isfile,join,getctime
from os import listdir,mkdir
from datetime import date
from random import randint

sessions_path = "/home/gsd/.sessions/"
notes_path = "/home/gsd/.nb/home/"
ctime_cookie_file = "/home/gsd/.config/sessions/cookie"
def get_new_notes(files):
    last_ctime = open(ctime_cookie_file, 'r').read()
    for file in files:
       ... 

def gen_data():
    for i in range(20):
        day = randint(1,31)
        month = randint(1,12)
        file_name = ''.join([sessions_path, str(day), '_', str(month)])
        print(file_name)
        f = open(file_name, 'w')
        f.write('TOREMOVE')
        f.close()        
today_day = date.today().strftime("%d")
today_month = date.today().strftime("%m")
today = today_day + "_" + today_month
try:
    listdir(sessions_path)
except FileNotFoundError:
    print("[!] directory does not exists on path yet, creating it...")
    mkdir(sessions_path)
session_files = [f for f in listdir(sessions_path) if isfile(join(sessions_path, f))]
for session in session_files:
    month = session.split('_')[1]
    day = session.split('_')[0]
    if int(month) >= int(today_month):
        if int(day) >= int(today_day):
            pass
    else:
        # TODO Informs user and add one week to system
        print('old file !')
# prev_sessions = [f for f in sessions_files ]
# TODO Informs user of the notes that aren't in the system
if today not in session_files:
    print("[+] today's session does not exists yet, creating from new notes...")
    generate_new_notes()
# TODO Get new notes
# TODO Run the session
# TODO Update the note value at each new note
