from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift):
    encoded_string  = ""
    for i, char in enumerate(message,0):
        if char == ' ':
            encoded_string+=' '
        else:
           
            x =  alphabet.index(char)
            
            x += int(shift)
            x = x%26
            
            encoded_string += alphabet[x]
    print(f"Your encoded message is {encoded_string}")

def decode(message, shift):
    decoded_string = ""
    for i,char in enumerate(message, 0):
        if char == ' ':
            decoded_string+=' '
        else:
            x = alphabet.index(char)
        
            x = x - int(shift)
            x = x%26
            decoded_string += alphabet[x]
    print(f"Your decoded message is {decoded_string}")

direction = input("Weather you want to encode the message or decode? ")
message = input("Type your message.")
shift = input("Enter the number of shifts ")

if direction == "encode":
    encode(message, shift)

else:
    decode(message, shift)