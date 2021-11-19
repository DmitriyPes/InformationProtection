def alphabet(int_key, str_key):
    a = ord('а')
    alphabet = ''
    for i in range(a, a + 33):
        alphabet = alphabet + ''.join(chr(i))
    print(alphabet)
    for sym in str_key:
        alphabet = alphabet.replace(sym, '')
    alphabet = str_key + alphabet
    print(alphabet)
    a = int_key % len(alphabet)
    alphabet = alphabet[-a:] + alphabet[:-a]
    return alphabet

if __name__ == '__main__':
    inp = "брух"
    int_key = 2
    str_key = "ха"
    abc = alphabet(int_key, str_key)
    message1 = ''
    for sym in inp:
        if sym.isalpha():
            message1 += abc[(ord(sym) - 224)%33]
        else:
            message1 += sym
    print(message1)
    print(abc)
