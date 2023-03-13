ComputerName = "Steve the Computer"
UserName = "Admin"


def UserInput():
    UserMsg = input(UserName + ": ")
    
    if UserMsg == "hello":
        print(ComputerName + ": Well, hello " + UserName + "!")
        UserInput()

    else if UserMsg == "goodbye":
        print(ComputerName + ": Goodbye " + UserName + "!")
        quit()

    else:
        print(ComputerName + ": Sorry, may you say that again?")
        if UserMsg == "no":
            print(ComputerName + ": goodbye :(")
            quit()
        UserInput()

if __name__ == "__main__":
    print(ComputerName + ": Hello boss! Welcome to your chatbot")
    print(ComputerName + ": My name is " + ComputerName + ", let's start a conversation")
    UserInput()
