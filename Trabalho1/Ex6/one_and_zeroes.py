# This helper function was put here to avoid mistakes
def calculate_lastindex(bit_sequence: list[int]): return len(bit_sequence) - 1


def padd_oneandzeroes(bit_sequence: list[int], n_bits: int):
    # Calculating how much bits to pad, and it is impossible to be 0, sinze we make the complement of the rest
    missing_bits = n_bits - (len(bit_sequence) % n_bits)

    # In this algorithm we fill one bit with one 1, and  then fill the rest with zeroes. In the case of having only
    # one place left before hitting n multiplicity our program does not enter the zeroes part

    bit_sequence.append(1)
    for i in range(1, missing_bits):
        bit_sequence.append(0)

    return bit_sequence


def unpadd_oneandzeroes(bit_sequence: list[int], n_bits: int):
    # This auxiliary function helps avoid mistakes
    lastitem_index = calculate_lastindex(bit_sequence)

    # This cycle iterates trough each step, and if the sequence ends with a one, it pops the one and returns. While the
    # sequence last position value is zero, the algorithm keeps popping until it finds a one, and then it enters the
    # first condition.
    for i in range(lastitem_index, lastitem_index - n_bits, -1):

        if bit_sequence[lastitem_index] == 1:
            bit_sequence.pop()
            return bit_sequence
        else:
            bit_sequence.pop()
            lastitem_index = calculate_lastindex(bit_sequence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(padd_oneandzeroes([0, 1, 0, 1, 1, 1, 1, 0, 1], 8))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
