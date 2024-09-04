import json # Importing this to convert dictionary objects into strings and strings back into dictionaries.

def signup():  # Creating a sign-up function that adds a new user with a name, username and password,
               # then I'll store this info in a dict and store each new dict in a file users.txt
    users = {}# I am initializing the dictionary which now is empty. It will store users' info later.

    name = input("Name: ")# This asks the user to input a name and stores it into the variable called name.
    username = userExists() #I am getting the username from the userExists function, which makes the user choose a username
                            #that doesn't exist already.
    password = input("Password: ")# This asks the user to input a password and stores it into the variable called password.
    
    users = {"name": name, "username": username, "password": password}# Here I am updating the dictionary with the info provided by the user.

    with open("users.txt", "a") as file: #This opens the txt file to append in it the data of the users variable.
        file.write(json.dumps(users) + "\n")#I am using \n to put each user data in a separate line (i.e. one line per user)
    print("You have successfully signed up")#This prints on screen when the signup is successful.


def login():  
    while True:#Used to reiterate the loop for the user's new input when needed.
        username = input("Username: ")#This asks the user to input their username and stores it into the variable username.
        with open("users.txt", "r") as file:#This opens the txt file to read it.
            users = file.readlines()#This reads all the lines in the file, and stores these into the variable users. I'll use this in the loop below.

        for userInfo in users: #For every line/string (named userInfo) in the file (every line is string information related to 1 user),
            user = json.loads(userInfo) #parse such line (which is in json) and convert it into a dictionary.
                                        #Assign such dictionary as the value of the user variable.
            if user["username"] == username: #If a username in one of these lines matches the username typed by the user,
                while True:  # (I am using a while loop so that the user gets asked for the password again if they type it incorrectly)
                    password = input("Password: ") #ask the user to type their password.
                    if user["password"] == password: #If the password in the txt matches the password typed by the user,
                        print("Welcome back " + user["name"] + "!") #Print on the screen a message of welcome back.
                        return  # This exits the loop
                    else:
                        print("Incorrect password. Try again.") # If the password typed doesn't have a match in the file,
                                                                #print a message on the screen and reiterate the password prompt msg again.                                                                
                break # This breaks when the correct password is entered.
            
        else: # If the username is not found in the file,
            print("Username not recognized. Try again.") # the user is asked to type it again.
    

def userExists():
            
    while True: # I am using a while loop for the user to be asked for a username again and again in case they type one that is already taken.
        username = input("Username: ")#This asks the user for a username and stores its value in the username variable.
        try:#I am using a try except so that if the file isn't found, the username isn't found either, which means that the username typed doesn't exist.
            with open("users.txt", "r") as file:#This tries to open the txt file and read it.
                users = file.readlines()#This reads all the lines in the file, and stores these into the variable users. I'll use this in the loop below.
        except FileNotFoundError: # If the file is not found,
            return username #return the username. I am using this logic because in this specific case
                            #if the file is not found it's because the txt file hasn't been created 
                            #(it will be created when the very first user signs up).

        for userInfo in users: #For every line/string (named userInfo) in the file (every line is string information related to 1 user),
            user = json.loads(userInfo)#parse such line (which is in json) and convert it into a dictionary.
                                        #Assign such dictionary as the value of the user variable.
            if user["username"] == username: #If a username in one of these lines matches the username typed by the user,
                print("Username already taken, choose another.")#inform them that such username is taken.
                break#This exits the loop and moves to prompting for a username again.

        else:#If not match is found,
            return username#return the username because it's not in the file, so it hasn't been taken already.

if __name__ == "__main__":  #I am calling the methods from the main method

    while True: #I am adding while true so that in case the user types any character other than l or s, the question gets reiterated
        userInput = input("Welcome! Press L to login or S to sign-up: ")
        if userInput == "L" or userInput == "l":
            login()
            break 
        elif userInput == "S" or userInput == "s":
            signup()
            break
        else:
            print("Invalid choice") #I didn't put any break in here so that when a character other than l or s is chosen, the Welcome message appears again
            
   
