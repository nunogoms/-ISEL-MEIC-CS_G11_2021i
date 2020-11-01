def generate_keystream(relation, initial_sequence, length):
    rotated_relation = []
    keystream = []

    # Append the initial given values to the generated keystream
    for i in range(0, len(relation)):
        keystream.append(initial_sequence[i])

    indexer = 0
    # We need to rotate the relation passed, because in the mathematical function , the values are given based on
    # actual position (Ie: K0 = (K-1) + (K-2) + (K-3)). If we want to access the elements in the array, we have to
    # consider the array positions (Ie: Array[(K-3), (K-2), (K-1), (K0)]. Since K0 depends on K3, K2 and K1,
    # it cannot be placed behind those values
    for i in range(len(relation) - 1, -1, -1):
        rotated_relation.append(relation[i])
        indexer += 1

    # Start to generate keystream
    for i in range(0, length - len(initial_sequence)):
        result = calculate(rotated_relation, initial_sequence)
        keystream.append(result)
        initial_sequence = refactor_initial_sequence(initial_sequence, result)

    return keystream


def calculate(rotated_relation, initial_sequence):
    aux = []
    indexer = 0

    # First of all, we perform an bitwise "AND" between the rotated relation and the values of the initial sequence
    for i in range(0, len(initial_sequence)):
        aux.append(initial_sequence[i] & rotated_relation[i])
        indexer += 1

    # Finally, to get the next bit of the keystream, we perform a bitwise "XOR" between the "AND" operation result
    # Current equals to -1 at the beginning to proceed with first "XOR" between the result of the "AND" between the
    # first two bits
    # Then, the result is stored and used to perform the "XOR" with the next bit of the previous "AND" operation
    current = -1
    while len(aux) > 0:
        if current == -1:
            current = aux.pop(0) ^ aux.pop(0)
        else:
            current = current ^ aux.pop()

    return current


# Once we have the next bit of the keystream, we need to perform a shift left operation in order to obtain the
# initial sequence with the calculated bit
def refactor_initial_sequence(initial_sequence, current):
    refactored = []
    if len(initial_sequence) - 1 >= 0:
        array_copy(initial_sequence, 1, refactored, 0, len(initial_sequence) - 1)

    refactored.append(current)
    return refactored


def array_copy(src, src_pos, dest, dest_pos, length):
    for i in range(0, length):
        dest.insert(i + dest_pos, src[i + src_pos])
