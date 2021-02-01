import csv
import json


def read_in_orig_file(orig_file, json_file):
    new_list = []
    fieldnames = ('username', 'fnamn', 'enamn', 'email')
    try:
        with open(orig_file, 'r', encoding="utf-8-sig") as f_obj:
            data = csv.DictReader(f_obj, fieldnames, delimiter=';')
            for entry in data:
                for category in entry:
                    entry[category] = entry[category].strip()
                new_list.append(entry)
            new_list.pop(0)
    except FileNotFoundError as ferr:
        print(ferr)
    try:
        with open(json_file, 'w', encoding="utf-8-sig") as f_obj:
            json.dump(new_list, f_obj)
    except FileNotFoundError as ferr:
        print(ferr)
    print('\n---- Dokumentet har mottagits ----')
    return new_list


def read_file(json_files):
    try:
        with open(json_files, 'r', encoding="utf-8-sig") as f_obj:
            data = json.load(f_obj)
        for row in data:
            print(row)
    except FileNotFoundError as ferr:
        print(ferr)


def add_person(people_list):
    username = ''
    fnamn = ''
    enamn = ''
    while not username:
        username = input('Användarnamn: ').strip()
    while not fnamn:
        fnamn = input('Förnamn: ').strip()
    while not enamn:
        enamn = input('Efternamn: ').strip()
    person = {'username': username, 'fnamn': fnamn, 'enamn': enamn, 'email': username + '@du.se'}
    people_list.append(person)
    print('\n---- Personen har lagts till i listan ----')
    return people_list


def remove_person(people_list):
    uname = input('Skriv in användarnamn på personen du vill ta bort: ')
    for i in range(len(people_list)):
        if people_list[i]['username'] == uname:
            del people_list[i]
            print(f'\n---- {uname} har tagits bort ----')
            break


def save_file(json_file, people_list):
    try:
        with open(json_file, 'w', encoding="utf-8-sig") as f_obj:
            json.dump(people_list, f_obj)
    except FileNotFoundError as ferr:
        print(ferr)
    print('\n---- Listan har sparats till saves.json ----')
