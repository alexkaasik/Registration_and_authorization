login = ["hulk","Flash"]
password = ["power","speed"]

def LP(L,P):
    LP = input("Login or Registration\n")
    if LP == "Registration" or LP == "R":
        L, P=registration(login,password)

    elif LP == "login" or LP == "l":
        L, P=Login(login,password)

    #to see what login and password there is
    elif LP == "sort":
        print(login)
        print(password)

    else:
        print("!ERROR!")

#randomize a password is 12 charcters long
def randomA():
    import random
    str0 = ".,:;! _ * - + () / # ¤% &"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper ()
    str4 = str0 + str1 + str2 + str3
    ls = list (str4)
    random.shuffle (ls)
    #Extract 12 random values ​​from the list
    psword = '' .join ([random.choice (ls ) for x in range (12)])
    # Password ready
    print (psword)
    password.append(psword)
    return login, password

def Login(login,password):
    print("Login Option")
    L = input("Input a username or email\n")
    while L not in login:
        L = input("Input a username or email \n")
    P = input("Input a password\n")
    while P not in password or password.index(P) != login.index(L):
        P = input("wrong password\n")

    print("Done")
    return login, password

def registration(login,password):
    print("Registration Option")
    L = input("Input a username or email\n")
    login.append(L)
    p = input("Automatic Password Generation(APG) or Independent\n")
    if p == "APG":
        p = randomA()
    else:
        Independent(login,password)
    return login, password

def Independent(login,password):
    print("Independent option")
    x = input("make a password 12 charters long\n")
    x2 = list(x)
    while len(x2) <= 12:
        print("bad")
        x2 = input("make a password 12 charters long\n")
    password.append(x)
    print("done")
    return login, password

while True:
    LP(login,password)