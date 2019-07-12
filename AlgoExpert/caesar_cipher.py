# T: O(n)
# S: O(n)

def caesarCipherEncryptor(string, key):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for c in string.lower():
        idx = (alphabet.index(c) + key) % len(alphabet)
        result += alphabet[idx]

    return result