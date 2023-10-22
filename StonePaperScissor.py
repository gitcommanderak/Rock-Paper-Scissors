import random
def gc():
    pc=input("Enter a choice (stone, paper, scissor):")
    options=["stone","paper","scissor"]
    cc=random.choice(options)
    choices={"pl":pc,"cp":cc}
    return choices
#def hi():
    return input("Enter a greeting:")
#resp=hi()
ch=gc()
#dict={"name": "aj", "Number": 1, "colour:": "blue", "choice": ch["pl"], "Greet": resp}
#dict2={"name": "aj", "Number": 0, "colour:": "red", "choice": ch["cp"], "Greet": resp}

def check(pc,cc):
    #print("You chose "+pc+", Computer chose "+cc)
    print(f"You chose {pc}, Computer chose {cc}")
    if pc==cc:
        return "Tie!"
    elif pc=="stone":
        if cc=="scissor":
            return "You Win!"
        else:
            return "You Lose!"
    elif pc=="paper":
        if cc=="stone":
            return "You Win!"
        else:
            return "You Lose!"
    elif pc=="scissor":
        if cc=="paper":
            return "You Win!"
        else:
            return "You Lose!"    
    else:
        return "Invalid Choice!!"
print(check(ch["pl"],ch["cp"]))