ComputerName = "Steve the Computer"
UserName = "Admin"


def UserInput():
    UserMsg = input(UserName + ": ")
    
    if UserMsg == "hello":
        print(ComputerName + ": Well, hello " + UserName + "!")
        UserInput()

    if UserMsg == "goodbye":
        print(ComputerName + ": Goodbye " + UserName + "!")
        quit()

    else:
        print(ComputerName + ": Sorry, may you say that again?")
        if UserMsg == "no":
            print(ComputerName + ": addios :(")
            quit()
        UserInput()


def Main():
    print(ComputerName + ": Hello boss! Welcome to your chatbot")
    print(ComputerName + ": My name is " + ComputerName + ", let's start a conversation")
    UserInput()

if __name__ == "__main__":    
    Main()
