askUser = input("1- Encrypt, 2- Decrypt: \n")

#Encryption
if askUser=='1':
    print("Caesar Cipher Encryption")
    message = input("Enter your message: ")
    encrypted_message = ""
    
    for x in message:
        code = ord(x)

        if 'a' <= x <= 'z':
            if code >= 120 :
                code = code - 23
                
            else:
                code = code + 3
            encrypted_message += chr(code)

        elif 'A' <= x <= 'Z':
            if code >= 88 :
                code = code - 23
             
            else:
                code = code + 3
            encrypted_message += chr(code)
            

    print("Original Message: ", message)    
    print("Encrypted Message: ", encrypted_message)

#Decryption
elif askUser=='2':
    print("Caesar Cipher Decryption")
    message = input("Enter your message: ")
    decrypted_message = ""
    
    for x in message:
        code = ord(x)

        if 'a' <= x <= 'z':
            if code <= 99 :
                code = code + 23
                
            else:
                code = code - 3
            decrypted_message += chr(code)
            
        elif 'A' <= x <= 'Z':
            if code <= 67 :
                code = code + 23
            else:
                code = code - 3
            decrypted_message += chr(code)        


    print("Original Message: ", message)    
    print("Decrypted Message: ", decrypted_message)
