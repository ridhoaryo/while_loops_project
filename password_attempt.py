password = '12345'
password_bool = False
input_password = input('input your password: ')
attempt = 1
while attempt != 4:
    if input_password != password:
        print('Password Incorrect')
        input_password = input('reinput your password: ')
        attempt += 1
    else:
        print('Password correct!')
        break