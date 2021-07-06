input ('Welcome to Jurassick Perk Online , Press Any Key to Create Account')

def add_user(store):
    user = input('Create Username: ')
    password = input('Create Password: ')
    if user in store:
        print ("That user already exsist")
        return False
    else:
        store[user] = password
        return True


global_store = dict()
for i in range(1000):
    add_user(global_store)
