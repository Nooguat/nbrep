import os
from datetime import date,datetime
from random import randint

# TODO Implement the read_cfg fonction
sessions = "/home/gsd/.sessions"
notes_dir = "/home/gsd/.nb/home/"
# Each line of the session file is made as filename:date:nb_rev_done:cur_speed

if os.name not in ['Linux', 'posix']:
    print('This script does not (yet) support other OS than Linux')
    raise OSError    
"""
    Return array with values from the config file if key is NULL, else return the value 
    linked to given key
"""
def read_cfg(key):
    ...
    
"""
    Return datetime object from delta added
"""
def compute_date(date_value, offset):
    date = datetime.strptime(date_value, "%d_%m")
    date = date + datime.timedelta(offset)
    # TODO Remove debug
    print(date)
    return date
# TODO Implement the read_cfg function

"""
    Return a factor based on how well the note was understood
"""

def get_understanding():
    respond = input("How well did you understood the note ? ")
    # TODO Implement the read_cfg function
    if respond in ['g', 'good', 'G']:
        return 2
    elif respond in ['o', 'ok','O']:
        return 1.5
    elif respond in ['b', 'B', 'bad']:
        return 1.25
    else:
        print("Sorry, input is invalid. Try o,b or g")
        # TODO Find a better way, unsure of behaviour is called too many times
        get_understanding()

"""
    Return n new notes from the vault
"""
def add_note():
    ...


"""
    Generate a new speed value based on the current speed, comprehension of user and how much 
    time this note has been reviewed. Not using a real algorithm for the moment
"""
def update_speed(cur_speed, nb_rep, compr_ratio):
    # TODO Work on a real algorithm
    return cur_speed * ( compr_ratio // (5/nb_rep))


"""
    Returns array of notes that needs to be review on that date or previously
"""
def get_review_notes(notes, date):
    res = []
    for note in notes:
        note_date = datetime.strptime(note.split(':')[1], "%d_%m")
        # TODO Notes before the current time should be splitted along the next way
        if note_date <= date:
            res.append(note)
    return res

"""
    Controls the daily session. Takes an array of notes in argument and read them one by one
"""    
def session(notes, session_file):
    for note in notes:
        values = note.split(':')
        # TODO Replace 5 by value in config
        if values[2] >= 5:
            print("This note has been reviewed a lot ! Please update knowledge graph when review is finished")
        speed = values[3]
        file = values[0]
        command = "speedread " + file + " -w " + speed
        os.system(command)
        speed = update_speed(speed, values[2], get_understanding())
        # TODO Create real model
        date = compute_date(values[1], (values[2]//10)*13)
        # TODO Find how the session file is updated with those new values + removing the one before

if __name__ == "__main__":
    # read_cfg
    with session_file as open(sessions, 'r+'):
        session(get_review_notes(session_file.read(), date.today(), session_file)

        