budget = int(input())
command = input()

while command != "End":
    product = int(command)
    budget -= product

    if budget < 0:
        print("You went in overdraft!")
        exit() #break
    command = input()
#else:
#    print("You bought everything needed.")
print("You bought everything needed.")