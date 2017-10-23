# Transposition Cipher
**Description:** This script with its associated Encrypter class takes an integer key and a message to either encrypt or decrypt using a transposition cipher. For Example, if a user were to input the key 5381 with the message "The eagle has landed." on the encrypt setting, it would be transposed by putting the message into a grid as follows:

5 3 8 1  
T h e    
e a g l  
e   h a   
s   l a  
n d e d  
.

The grid is completed by padding with spaces. After the grid is created, the cipher text is rendered by reading down the columns in the order dictated by the key. In this case starting with the column with the 1 heading followed by 3, 5, and 8. Colons are entered to mark the beginning and end of the cipher text. The cipher text for our example, therefore, would be:

: laad ha  d teesn.eghle :

To decrypt, the decrypt option can be entered at runtime and the key with the cipher text(including colons) and the plaintext will be generated.

**Notes:** Please note that the purpose of this module is education and not transmitting secure messages. This is considered a weak cipher unless both the key and the message are quite long.  

**Usage:** To use the cipher, clone the repository and run encrypt.py. You can then follow the prompts to encrypt and decrypt.
