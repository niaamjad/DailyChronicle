import datetime
users = {}
current_user = None
memories = {}

def register():
    global users
    username = input('add your username: ')
    if username in users:
        print('This username already exists. Please choose another one.')
        return
    password = input('Your password: ')
    users[username] = password
    memories[username] = []
    print('Registration was successful!')

def login():
    global current_user
    username = input('username: ')
    password = input('password: ')
    if users.get(username) == password:
        current_user = username
        print(f'welcome , {username}!')
    else:
        print('Your username or password is incorrect. Please try again.')

def logout():
    global current_user
    current_user = None
    print('logout was successful!')

def add_memory():
    if not current_user:
        print('Please log in first.')
        return
    title = input('Your memory title: ')
    content = input('Your memory content: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    memories[current_user].append({
        'title': title,
        'content': content,
        'date': date
    })
    print('Your memory has been added successfully!')
 
def show_memories():
    if not current_user:
        print('Please log in first.')
        return
    print(f'\Memories {current_user}:')
    for i, memory in enumerate(memories[current_user]):
        print(f'{i+1}. {memory['title']} - {memory['date']}')
        print(memory['content'])
        print('-' * 10)

def delete_memory():
    if not current_user:
        print('Please log in first.')
        return
    show_memories()
    index = int(input('Number of memory for deleting')) - 1
    if 0 <= index < len(memories[current_user]):
        del memories[current_user][index]
        print('Memory deleted successfully!')
    else:
        print('No memory found with that number!')

def main():
    while True:
        print('\n--- Main Menu ---')
        print('1. Register')
        print('2. Sign in')
        print('3. Sign out')
        print('4. Add memory')
        print('5. Show memories')
        print('6. Delete memory')
        print('7. Exit')
        choice = input('Please choose an option: ')

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            add_memory()
        elif choice == '5':
            show_memories()
        elif choice == '6':
            delete_memory()
        elif choice == '7':
            print('Exit from the program.')
            break
        else:
            print('Not a valid choice, please try again.')

if __name__ == '__main__':
    main()
