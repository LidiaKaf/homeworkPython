def func():
    user = {'name': '','surname': '','birth_year': '','city': '','email': '','phone_num':''}
    for key, value in user.items():
        value = input(f'enter your {key} - ')
        user[key] = value
    return user


user = func()
print(' '.join(list(user.values())))
