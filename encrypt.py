from Encrypter import encrypter

"""
Title: Transposition Cipher
Last Edited: 10/23/2017
Author: Joseph Potter
Description: See README
"""
Continue = True
while Continue:
    Encrypter = encrypter()
    choice = input("Would you like to decrypt or encrypt?(e/d): ")
    Encrypter.get_key()
    if choice == 'e':
        Encrypter.get_variables(input("Enter message: "),0)
        print ("Cipher Text:")
        print(Encrypter.encrypt())
    else:
        Encrypter.get_variables(input("Enter message: "),2)
        print ("Plain Text:")
        print(Encrypter.decrypt())
    continue_choice = input("Would you like to keep going?(y/n)")
    if continue_choice not in ['y', 'Y']:
        Continue = False
