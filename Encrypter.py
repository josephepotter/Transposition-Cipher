"""
Title: Transposer
Last Edited: 10/23/2017
Author: Joseph Potter
Description: This Class applies a transpostition cipher to a message append
encryption key for encyrypting or decrypting.
"""
class encrypter():
    message = ''
    key = ''
    message_length = 0
    key_length = 0
    mod = 0
    row_count = 0
    strings = []
    control_dict = {}
    digits = []
    def get_key(self):
        key = input("Please input an integer key:")
        exit = False
        while exit == False:
            try:
                int_key = int(key)
                exit = True
            except:
                key = input("That was not an integer. Please try again:")
        self.key =  str(key)
    def get_variables(self, message, strip_letters):
        self.message = message
        self.message_length = len(message) - strip_letters
        self.key_length = len(self.key)
        self.mod = self.message_length % self.key_length
        self.row_count = int(self.message_length / self.key_length)
        self.strings = []
        self.control_dict = {}
    def encrypt(self):
        position = 0
        for i in range(self.row_count):
            #Slice the message up into chunks
            self.strings.append(
                    self.message[position:position + self.key_length]
            )
            position += self.key_length
        #add the leftover characters
        self.strings.append(self.message[position:position + self.mod])
        for i in range(self.key_length - self.mod):
            #make the last character the same length
            self.strings[self.row_count] += ' '
        cipher_text = ':'
        self.load_control_dict('e')
        for i in range(self.key_length):
            #create the cipher text based on the control_dict created from key.
            for s in self.strings:
                cipher_text += s[self.control_dict[i]]
        return cipher_text + ':'
    def load_control_dict(self, e_or_d):
        digits = []
        for i in range(self.key_length):
            digits.append(int(self.key[i]))
        for i in range(len(self.key)):
            min_pos = 0
            for j in range(len(digits)):
                if digits[j] < digits[min_pos]:
                    min_pos = j
            digits[min_pos] = 10
            if e_or_d == 'e':
                self.control_dict[i] = min_pos
            else:
                self.control_dict[min_pos] = i
    def decrypt(self):
        #take off the leading and tailing colons
        self.message = self.message[1:len(self.message) -1 ]
        self.load_control_dict('d')
        for i in range(self.row_count):
            #create a list of strings of appropriate length
            self.strings.append('')
        for i in range(self.key_length):
            #preform the invers operation
            for j in range(self.row_count):
                self.strings[j] += (
                        self.message[(self.row_count)*self.control_dict[i] + j]
                )
        plaintext = ''
        for s in self.strings:
            plaintext += s
        return plaintext
