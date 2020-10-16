#Validate credit cards using Luhn's algorithm. Input should be 16 digits.

def luhn():
    card_number=input("Enter the card number to be checked: ")
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd = digits[-1::-2]
    even = digits[-2::-2]
    checksum = 0
    checksum += sum(odd)
    for d in even:
        checksum += sum(digits_of(d*2))
    if (checksum % 10):
        print("\nThis card is INVALID.")
    else:
        print("This card is VALID.")
    again = input("\nDo want to input another card?(y/n)")
    if (str(again)).lower() == "y":  
        luhn()

if __name__ == "__main__":
    luhn()