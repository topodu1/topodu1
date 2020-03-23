#Python User Data Validation Task11111
#By: Temitope Odulate
#email: topeodulate@gmail.com

#First I import random and strings as I need them for this program
import random
import string

#function to get user information
def get_info():
    first_name = input("what is your first name? ")
    last_name = input("what is your last name? ")
    email = input("what is your email address? ")
    info = [first_name, last_name, email]
    return info


#function to get 5 random characters
def random_password(info):
    character = string.ascii_lowercase
    length = 5
    random_pwd_gen = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    password = str(info[0][0:2] + info[1][-2:] + random_pwd_gen)
    return password


#Container Creation with empty info and Start of Data Validation Program
status = True
container = []

while status:
    #User Information
    info = get_info()

    #generated password
    password = random_password(info)
    print('your password is ' +  password)

    #prompt user if password is satisfactory and would like to continue
    user_pwd_like = input('''do you like your password? '
                             If Yes, type Yes   
                             If No, type No and enter your preferred password   
                                ''')
    pwd_loop = True

    while pwd_loop:

        #If user likes password, add password to user information
        if user_pwd_like.lower() == "yes":
            info.append(password)

            #add user data to overall container
            container.append(info)
            pwd_loop = False
            break

        else:
            #ask user to enter a password not less than 7 characters
            new_password = input("Enter your preferred password, not less than 7 characters ")

            #loop to check password length
            pass_len = True
            while pass_len:
                #add password to user information
                if len(new_password) >= 7:
                    info.append(password)

                    # add user data to overall container
                    container.append(info)
                    pwd_loop = False
                    pass_len = False
                    break
                else:
                    #promots user to enter another password that has at least 7 characters
                    print("oops, your password is less than 7 characters 😔 ")
                    new_password = input(str("Enter your preferred password, not less than 7 characters "))


    #New User Information Data Prompt
    new_user = input("Would you like to Enter a new user information? Yes or No? ")
    if (new_user == "No"):
        #End program and print all stored information
        status = False
        for data in container:
            print(data)