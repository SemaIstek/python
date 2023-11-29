import random
import string
pw=[]
name= input("Enter your name")
def generatepass():
    while(len(pw)<15):
        pw.append(str(random.randint(1,10)))
        pw.append(random.choice(string.ascii_lowercase))
        pw.append(random.choice("!.,-_"))
    print(pw)

generatepass()
print("Your name: ", name)
print("Your password:", "".join(map(str,pw)))
    


