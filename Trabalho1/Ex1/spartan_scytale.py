# clear_text stands for the the text to cipher,
# n stands for the width of the scytale
def spartan_scytale(clear_text: str, n: int):
    # We have to know the size of each line, since they have to be divided into the width of scytale to align
    # correctly when it is time to put them together
    line_size = int((len(clear_text) / n) + 0.5)

    # The array that will hold the multiple lines arranged for the "scytale"
    lines_array = []

    # Dividing the full text into n sections, so they allign
    for i in range(0, n):
        maxsize = line_size * (i + 1)
        lines_array.append(clear_text[i * line_size:maxsize])

    # The variable that will hold the final cyphered text
    cipher_text = ""

    # Iterating over index of the divided lines, so each position aligns with each other, being all the index=1 letters,
    # then the index = 2 and so on and so forth, as if they were written on a cloth and wrapped on a scytale
    for i in range(0, line_size):
        for line in range(0, len(lines_array)):
            if len(lines_array[line]) > i:
                cipher_text += lines_array[line][i]

    return cipher_text.upper()


def testing():
    # Exercise 1.a) Example
    entry1 = "abatalhacomospersasteralugarnodesfiladeirodastermopilas"
    n1 = 4
    result1 = "AENDBROAASDSTAETASSELTFRHEIMARLOCAAPOLDIMUELOGIASARSPRO"
    assert spartan_scytale(entry1, n1) == result1, "Should be : " + result1

    # A powerpoint example
    entry2 = "acitalaeumsistemadecifrausadonaantigagrecia"
    n2 = 5
    result2 = "AMEDACSCOGIIINRTSFAEATRACLEANIAMUTAEASIUDAG"
    assert spartan_scytale(entry2, n2) == result2, "Should be : " + result2


if __name__ == '__main__':
    testing()
