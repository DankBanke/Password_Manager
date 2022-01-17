import Passwords as Pass

password = Pass.Passwords()

while True:
    try:
        user_input = int(input('''
-Terminate program[0]
-Generate new password from keyword[1]
-Retrieve password with keyword[2]
-Create new file (WARNING: FIRST-TIME USERS ON THIS SYSTEM ONLY! 
IF YOU HAVE ALREADY CREATED A FILE WITH PASSWORDS IN IT,
THIS FUNCTION WILL WIPE ALL YOUR PASSWORDS! )[3]
> '''))
        if user_input == 1:
            old_pass = input("Keyword:  ").lower()
            new_pass = password.generate(old_pass)
            password.store(old_pass, new_pass)
            print(f'This is your new password: {new_pass}')
        elif user_input == 2:
            keyword = input('Keyword: ').lower()
            key_pass = password.get_pass(keyword)
            print(f"Your {keyword} password: {key_pass}")
        elif user_input == 3:
            yn = input("ARE YOU SURE?[y/n]").lower()
            if yn == 'y':
                msg = password.create_file()
                print(msg)
            else:
                pass
        elif user_input == 0:
            break
    except ValueError:
        print('Invalid Input')