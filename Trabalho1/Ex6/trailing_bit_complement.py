# This helper function was put here to avoid mistakes
def calculate_lastindex(bit_sequence: list[int]): return len(bit_sequence) - 1


def padd_trailingbitcom(bit_sequence: list[int], n_bits: int):
    # Calculating how much bits to pad, and it is impossible to be 0, since we make the complement of the rest
    missing_bits = n_bits - (len(bit_sequence) % n_bits)

    # We calculate the complement bit, by subtracting one, to whichever is the last bit. Since the complement is the
    # opposite of the last value, this subtraction does it.
    complementbit = 1 - bit_sequence[calculate_lastindex(bit_sequence)]

    # We apply the complement to the list, as much times as there are missing bits
    for i in range(0, missing_bits):
        bit_sequence.append(complementbit)

    return bit_sequence


def unpadd_trailingbitcom(bit_sequence: list[int], n_bits: int):
    # It is found which is the last bit, and therefore the bit being used as the complement bit
    complementbit = bit_sequence[calculate_lastindex(bit_sequence)]

    # Only used to count the ammount of iterations made
    i = 0

    # We keep removing numbers until we find the first number that is different from the complement bit, or we reach the
    # maximum ammount of allowed padding which is n.
    while bit_sequence[calculate_lastindex(bit_sequence)] == complementbit:
        i += 1
        bit_sequence.pop()

        # Used to avoid badly padded cases
        if i % n_bits == 0:
            return bit_sequence

    return bit_sequence


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(unpadd_trailingbitcom([0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 8))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
