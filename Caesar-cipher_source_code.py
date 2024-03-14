alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
        88             88       
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88 
      
      
      ''')


def caesar(plain_text,shift_amount,Direction):
  end_text = ""
  if direction == 'decode':
      shift_amount = shift_amount * - 1
  for char in plain_text:
    if char in alphabet:
      position = alphabet.index(char)
        
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char 
  print(f"The {Direction}d text is {end_text}")

choice = 'yes'
while(choice != 'no'):
    choice = input("Do you want to use the CAESAR CIPHER? Type 'yes' or 'no'.\n")
    if choice == 'no':
       print("Goodbye! ;)")
       exit()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and "decode":
        print("Please enter the appropriate command!")
        break
    
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26

    caesar(plain_text=text,shift_amount=shift,Direction=direction)



