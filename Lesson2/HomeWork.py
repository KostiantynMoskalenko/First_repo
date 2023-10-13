message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if (ord (ch) >=97 and ord (ch) <=123):
        pos = ord(ch) - ord('a')
        pos = (pos + offset) % 26 
        encoded_message += chr(pos + ord('a'))
    elif (ord (ch) >=65 and ord (ch) <=91):
        pos = ord(ch) - ord('A')
        pos = (pos + offset) % 26 
        encoded_message += chr(pos + ord('A'))
    else:
        encoded_message += ch
print(encoded_message)