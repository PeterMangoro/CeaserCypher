def ceaserDecrypt():
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'


    string_input = input('Enter text for decryption: ')
    string_input = string_input.lower()
    key = int(input('Enter key: '))

    n = len(string_input)
    string_output = ''

    for i in range(n):

        character = string_input[i]
        location = alpha.find(character)
        newLocation =(location - key)% 36
        string_output += alpha[newLocation]

    print('Decrypted message : '+ string_output)
    prompt = input('Do you want to write another message [Y/N] : ')
    prompt = prompt.upper()
    if prompt == 'Y' or prompt == 'YES':
        ceaserDecrypt()
    elif prompt == 'NO' or prompt == 'N':
       suggestion = input('do u want to encrypt instead ?  [Y/N]: ')
       suggestion = suggestion.upper()
       if suggestion == 'YES'  or suggestion == 'Y':
        ceaserEncrypt()
       else :
           print('Thank you ')


def ceaserEncrypt():
    
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'


    string_input = input('Enter text for encryption: ')
    key = int(input('Enter key: '))

    n = len(string_input)
    string_output = ''

    for i in range(n):
        character = string_input[i]
        location = alpha.find(character)
        newLocation =(location + key)% 36
        string_output += alpha[newLocation]

    print('Encrypted message : '+ string_output)
    prompt = input('Do you want to write another message [Y/N] : ')
    prompt=prompt.upper()
    if prompt == 'Y' or prompt == 'YES':
        ceaserEncrypt()
    elif prompt == 'NO' or prompt == 'N':
       suggestion = input('do u want to decrypt instead ? [Y/N] : ')
       if suggestion == 'YES' or suggestion == 'Y':
        suggestion = suggestion.upper()
        ceaserDecrypt()
       else :
           print('Thank you ')

def Prompt() :

    Qsn =input('Hie , do u want to encrypt or decrypt [E/D] : ')
    Qsn = Qsn.upper()

    if  Qsn == 'ENCRYPT' or Qsn== 'E' :
     ceaserEncrypt()

    elif Qsn== 'DECRYPT' or Qsn == 'D' :
     ceaserDecrypt()

Prompt()



