
def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]   
name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
