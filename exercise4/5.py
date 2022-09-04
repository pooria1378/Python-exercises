correct_username = 'python'
correct_password = 'rules'
rounds = 1
print(f"*********************************** rounds:{rounds} ********************************************")
username = input('enter username : ')
password = input('enter password : ')

while True:
    rounds += 1
    if username.lower() == correct_username and password == correct_password:
        print('welcome!')
        break
    elif rounds < 6:
        print(f"*********************************** rounds:{rounds} ********************************************")
        username = input('enter username : ')
        password = input('enter password : ')
    else:
        print('access denied')
        break
