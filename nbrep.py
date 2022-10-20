from os.path import isfile,join,getctime
from os import listdir,mkdir,system
from os import name as pname
from datetime import date,datetime
from random import randint

speed_date_link = []

if pname not in  ['Linux', 'posix']:
    print("This script is not (yet) running on other systems than Linux !")
    print(pname)
    exit()

sessions_path = "/home/gsd/.sessions/"
notes_path = "/home/gsd/.nb/home/"
list_known_files = "/home/gsd/.config/sessions/cookie"
# TODO Add notes based on the getctime value 



def compute_date(date, speed, understood):
    # TODO Find a way to tell it note has been graphed
    if speed == -1:
        speed = 1000
    new_rev = datetime.strptime(date, "%d_%m")
    new_speed = speed*understood
    nb_days = round(new_speed / 100) # Very approx, will need some tweaking
    print(nb_days)
    new_rev = new_rev + datetime.timedelta(days=nb_days)
    res = new_rev.strftime("%d_%m")
    res = res + ':' + new_speed
    return res

"""
    Get the list of notes that are not in the review process and return the list of 
    n of those notes ; adding them to the system
"""
def get_new_notes(files, n : int):
    res = []
    with open(list_known_files, 'r+') as known_file:
        content = known_file.read()
        for f in files:
            if f not in content:
                print("[+] Adding new file to note")
                res.append(f)
                known_file.write(f+'\n')
                if len(res) == n or len(res) == 10:
                    return res
        return res
            
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
notes = [f for f in listdir(notes_path) if isfile(join(notes_path, f))]
for session in session_files:
    month = session.split('_')[1]
    day = session.split('_')[0]
    # TODO Informs user and add one month after current month to system
    if int(month) <= int(today_month):
       if int(day) >= int(today_day):
            continue
         # TODO Implement menu 
         # print("[!] Found a session file older than today. What do you want to do with that ?")       
       # print("month : ",month,"/",today_month," ",day,"/",today_day)
# if today not in session_files:
#     print("[+] today's session does not exists yet, creating from new notes...")
    # get_new_notes(notes, 7)
# TODO Run the session
with open(sessions_path+today, 'r+') as cur_review:
    for line in cur_review.readlines():
        note = notes_path+line.split(":")[0]
        # TODO Check that the file still exists in filesystem
        speed = line.split(":")[1]
        if speed == -1:
            print("[!] This note has been enough reviewed using dynamic reading")
            print("[+] Now try to graph your knowledge about : ", note)
        else:
            command = "speedread " + note + " -w " + speed
            system(command)
        i = input("[?] Did you understood the note content ? ")
        if i not in ["y", "Y", "n", "N"]:
            i = input("[?] Did you understood the note content ? ")
        # TODO Algorithm to determine next review date
        if i == 'y' or i == 'Y':
            res = compute_date(cur_review, speed, 2)
        else:
            res = compute_date(cur_review, speed, 1.25)
# TODO Update the note value at each new note
