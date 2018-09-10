# Procedure to find ticket price based on age
def ticket_price(alder):

    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50
    
    print("For age %d, the price is %d" % (alder, billettpris))
    return billettpris

# The problem arises when checking for two conditions that are greater than some number, without any ceiling
# This is because they are both true, making it run through both statements
# However, I saw this problem before reading the last task
# I believe I have a good solution for what I interpreted as the correct intention

for i in range(0,4):
    ticket_price(int(input("Enter age to get the correct price: ")))
