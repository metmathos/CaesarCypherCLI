"""
CAESAR CIPHER

Author: Matias Eduardo Herrera
Date: 2024-10-05
Version: 1.0


CLI version for a simple Caesar encription of a text

Features:
 * Encode and decode a message
 * Shift the alphabet a certain number of positions

Possible Improvements:
    *Add support for file input/output
    *Add option to handle non-alphabetic characters
    *GUI version using Tkinter or PyQt
"""

def encode(shift:int, message:str, c_message:list, alpha:list): 
    ''' Method for encoding'''
    for let in message:
        for index,letter in enumerate(alpha):
            full_shift = index + shift
            while(full_shift>=26):
                full_shift -= 26
            if let == letter:
                c_message.append(alpha[full_shift])
        if let not in alpha:
            c_message.append(let)

    encoded_message = "".join(c_message)
    print(f"Here's the encoded result: {encoded_message}")

def decode(shift:int, message:str, c_message:list, alpha:list):
    '''Method for decoding''' 
    for let in message:
        for index,letter in enumerate(alpha):
            full_shift = index - shift
            while(full_shift < 0):
                full_shift = 26 + full_shift
            if let == letter:
                c_message.append(alpha[full_shift])
        if let not in alpha:
            c_message.append(let)

    decoded_message ="".join(c_message)
    print(f"Here's the decoded result: {decoded_message}")
            

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cripted_message = []

again = 'yes'

while(again == 'yes'):
    while True:
        mode = input("Type 'encode' to encrypt or 'decode' to decrypt:")
        mode = mode.lower()
        if (mode=="encode" or mode=="decode"):
            break
        else:
            print("Please, enter a valid input")


    message = input("Type your message:\n")
    message = message.lower()

    while True:
        shift = input("Type the shift number:\n")
        if (shift.isdecimal()):
            shift = int(shift)
            break
        else:
            print("Please, enter a valid integer\n")


    if (mode == 'encode'):
        encode(shift, message, cripted_message, alphabet)
    elif (mode == 'decode'):
        decode(shift, message, cripted_message, alphabet)

    cripted_message = []

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    while (again != "yes" and again != "no"):
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if again == "no":
        break