# First, create a map to store the matches of the used alphabet, and the indexes of the considered domain
# In this case, the domain is the standard alphabet, using indexes from 0 to 25
def populate_map():
    mapping = []
    for i in range(0, 26):
        mapping.insert(i, chr(ord('a') + i))

    return mapping


# Find the matches between the plain text, the key and the previously populated map
# Perform one run over the plain text, and readjust the "j" index to iterate over the correct positions of the key
# If the sum of both indexes is equal or over 26, it means that we overpassed the domain range, there for, we need to
# go back to zero. We can do this, by finding the remainder of the division by 26 (for this specific domain)
def belaso_vigenere(clean_text, key):
    mapping = populate_map()
    built_cipher = []
    j = 0

    for i in range(0, len(clean_text)):
        index = mapping.index(clean_text[i].lower()) + mapping.index(key[j].lower())
        if index >= 26:
            code = index % 26
        else:
            code = index

        built_cipher.append(code)
        j += 1
        if j == len(key):
            j = 0

    return ciphered_text(built_cipher, mapping)


# Find the matches between the ciphered text characters code, and the initial built map to obtain the final
# encrypted text
def ciphered_text(built_cipher, mapping):
    cipher = []
    for i in range(0, len(built_cipher)):
        cipher.append(mapping[(built_cipher[i])].upper())

    return cipher
