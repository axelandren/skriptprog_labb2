import modules
ORIG_FILE = 'labb2-personer.csv'
JSON_FILE = 'saves.json'
people_list = []


while True:
    print('\n1. Läs in filen labb2-personer.csv')
    print('2. Visa listan')
    print('3. Visa json-filen')
    print('4. Lägg till person')
    print('5. Ta bort person')
    print('6. Spara fil')
    print('7. Avsluta')
    choice = input('Välj ditt alternativ: ')
    if choice == '1':
        people_list = modules.read_in_orig_file(ORIG_FILE, JSON_FILE)
    elif choice == '2':
        if len(people_list) > 0:
            for person in people_list:
                print(person)
        else:
            print('\n---- Listan har inget innehåll ----')
    elif choice == '3':
        modules.read_file(JSON_FILE)
    elif choice == '4':
        people_list = modules.add_person(people_list)
    elif choice == '5':
        modules.remove_person(people_list)
    elif choice == '6':
        modules.save_file(JSON_FILE, people_list)
    elif choice == '7':
        print('\n---- Avslutar ----')
        break
    else:
        print('\n---- Ogiltigt svar ----')
