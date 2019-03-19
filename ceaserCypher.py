def ceaser():
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'


    string_input = input('Enter text for encryption: ')
    key = int(input('Enter key: '))

    n = len(string_input)
    string_output = ''

    for i in range(n):
        character = string_input[i]
        location = alpha.find(character)
        newLocation =(location + key)% 26
        string_output += alpha[newLocation]

    print('Encrypted message : '+ string_output)

ceaser()