import sys

def encrypt_string(str):
    encrypted = ""
    for char in str:
        encrypted += chr(ord(char) + 1)
    return encrypted

def decrypt_string(en_str):
    decrypted = ""
    for char in en_str:
        decrypted += chr(ord(char) - 1)
    return decrypted

def main():
    print("""
    
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗   
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝   
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║      
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║      
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║      
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ██║   ╚═╝        ╚═╝      
                                                               
██╗   ██╗ ██████╗ ██╗   ██╗██████╗                             
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗                            
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝                            
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗                            
   ██║   ╚██████╔╝╚██████╔╝██║  ██║                            
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                            
                                                               
███╗   ███╗███████╗███████╗███████╗ █████╗  ██████╗ ███████╗██╗
████╗ ████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝██║
██╔████╔██║█████╗  ███████╗███████╗███████║██║  ███╗█████╗  ██║
██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══██║██║   ██║██╔══╝  ╚═╝
██║ ╚═╝ ██║███████╗███████║███████║██║  ██║╚██████╔╝███████╗██╗
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝

    """)

    choice = input("Do you want to encrypt or decrypt message? ")
    if choice.lower() == "encrypt":
        msg = input("Enter the message: ")
        print(f"Encrypted Message: {encrypt_string(msg)}")

    elif choice.lower() == "decrypt":
        msg = input("Enter the encrypted message: ")
        print(f"Decrypted Message: {decrypt_string(msg)}")

    else:
        print("Invalid option!", file=sys.stderr)

if __name__ == "__main__":
    main()
