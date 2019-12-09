
# Zendesk Coding Challenge 

# Write an `encrypt` and a `decrypt` method. Each should accept a `key` and a `message`.
# 
# encrypt(key, message) should reorder the alphabet by moving the key's letters to the front and return a string with the old string's letters swapped out for their index in the new alphabet. If you were encrypting a message by hand, you would take each letter in your message, find it in the top line, and swap it for the letter at the same position in the bottom line. Assume that keys will not contain the same letter more than once.
# 
# 
# abcdefghijklmnopqrstuvwxyz
# thingsabcdefjklmopqruvwxyz
# 
# 
# The encrypt method should return "rbgqg tpg qljg wlpnq".
# 
# def encrypt(“things”, “these are some words”):
#   ...
# => "rbgqg tpg qljg wlpnq"
# 
# 
# Decrypt just reverses the process:
# 
# def decrypt(“things”, “rbgqg tpg qljg wlpnq”):
#   ...
# => "these are some words"
# 
# 
# Use any language you like. Google any documentation you want, but no complete solutions. You’re encouraged to ask clarifying questions.
# 
# Prioritize a complete solution first. We’re most interested in the readability and completeness of your solution, and much less concerned with its performance.

# Create an alphabet Dictionary where 
# Create the new alphabet

alphabet_dict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
        'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 
        'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 
        'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 
        'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25} 

alphabet = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
            7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
            14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
            21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}       

def encrypt_and_decrypt(key, msg):
    message = msg.upper()
    new_alphabet = {}
    enc_msg = ''
    decode = ''
    temp_dict = alphabet.copy()

    for i in key.upper():
      key_indexes = alphabet_dict[i] 
      del temp_dict[key_indexes]
      all_vals = temp_dict.values()

    for j in range(len(key)):
      if key[j] not in alphabet_dict:
          letters = key[j].upper()
          new_alphabet[j] = letters
    length = len(new_alphabet) - 1
   
    for v in all_vals:
      if v not in new_alphabet:
        length += 1
        new_alphabet[length] = v

    for char in message:
      if (char != ' '):
        num = alphabet_dict[char]  
        enc_msg += new_alphabet[num]
        decode += alphabet[num]
        
    return enc_msg, decode
    
