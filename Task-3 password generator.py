import string
import random
if __name__== "__main__":
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all = lower + upper + digits +  punctuation
    length=int(input("Enter the Length of Password:"))
    password = "".join(random.sample(all,length))
    print(password)
    length=int(input("Enter the Length of Password:"))
    password = "".join(random.sample(all,length))
    print(password)
    print("Gnerated random Password")
    

