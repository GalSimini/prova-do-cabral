found = []
searching = ['a' , 'ab' , 'aba' , 'aaab' , 'bbbbb']

def recursive_string(repeats, string=''):
    if repeats == 0:
        return [string]

    if string in searching:
        found.append(string)

    if string == '':
        return recursive_string(repeats - 1, 'a') + recursive_string(repeats - 1, 'b')

    else:
        return recursive_string(repeats - 1, string + 'b')

print(recursive_string(10))
print(f"Encontrado: {found}")