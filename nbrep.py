import os
from datetime import date,datetime,timedelta
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
    date = datetime.strptime(date_value, "%d_%m_%y")
    date = date + timedelta(offset)
    # TODO Remove debug
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
        print("Sorry, input is invalid. Try b,o or g")
        # TODO Find a better way, unsure of behaviour is called too many times
        get_understanding()

"""
    Return n new notes from the vault
"""
def add_note(nbr_notes,rev_file):
# TODO Setup case of no new notes to add
    notes = [f for f in os.listdir(notes_dir) if os.path.isfile(os.path.join(notes_dir, f))]
    counter = len(rev_file.readlines())+1
    rev_notes = [f.split(':')[0] for f in rev_file.readlines()]
    indexes = []
    for n in notes:
        if n not in rev_notes:
            if counter <= nbr_notes:
                entry = ':'.join([n,date.today().strftime('%d_%m_%y'),'0','350\n'])
                rev_file.write(entry)
                indexes.append(counter)
                counter+=1
    if len(indexes) < nbr_notes :
        print("Not enough notes to complete order ! Write more") 
    return indexes

"""
    Generate a new speed value based on the current speed, comprehension of user and how much 
    time this note has been reviewed. Not using a real algorithm for the moment
"""
def update_speed(cur_speed, nb_rep, compr_ratio):
    # TODO Work on a real algorithm
    cur_speed = int(cur_speed)
    nb_rep = int(nb_rep)
    cur_speed *= ( compr_ratio // (5/nb_rep))
    return str(cur_speed)


"""
    Returns array of indexes of the lines that need to be review on that date. 
    If any notes that needed to be reviewed previously is found, it is updated to match the next 
    week of the current date
"""
def get_review_notes(notes, date):
    # TODO This should be more flexible
    res = []
    index = 0
    for note in notes:
        if ':' not in note:
            print('this line is not well formatted, skipping...')
            continue
        note_date = datetime.strptime(note.split(':')[1], "%d_%m_%y").date()
        # TODO Notes before the current time should be splitted along the next week
        if note_date == date:
            res.append(index)
        elif note_date < date:
            print("This note should have been reviewed before, adding it along the next week")
        index += 1
    return res

"""
    Controls the daily session. Takes an array of notes in argument and read them one by one
"""    
def session(notes_index, session_file):
    for index in notes_index:
        print(session_file[index])
        values = session_file[index].split(':')
        # TODO Replace 5 by value in config
        date = values[1]
        file = values[0]
        nbr_seen = values[2]
        speed = values[3]
        if int(nbr_seen) >= 5:
            print("This note has been reviewed a lot ! Please update knowledge graph when review is finished")

        command = "speedread " + notes_dir + file + " -w " + speed
        # os.system(command)
        nbr_seen = str(int(nbr_seen) + 1)
        speed = update_speed(speed, nbr_seen, get_understanding())
        # TODO Create real model
        date = compute_date(date, (int(nbr_seen)//10)*13).strftime("%d_%m_%y")
        # TODO Find how the session file is updated with those new values + removing the one before
        n_review = ':'.join([file, date,nbr_seen, ])
        print(n_review)
        session_file[index] = n_review
    print("Review is done for today !")
    return session_file

if __name__ == "__main__":
    # TODO read_cfg
    with open(sessions, 'r+') as session_file:
        base_review = get_review_notes(session_file.readlines(), date.today())
        # TODO What if base_review == 0 ?
        if len(base_review) < 8:
            print("Few notes are to review today, adding new ones from vault...")
            base_review += add_note(8-len(base_review),session_file)
        else:
            base_review += add_note(2, session_file)
    with open(sessions, 'r+') as session_file:
        n_file = session(base_review, session_file.readlines())
        session_file.write('\n'.join(n_file))

        