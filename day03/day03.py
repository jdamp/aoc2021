from collections import Counter

def gamma(bitstr):
    return(int(bitstr, 2))

def epsilon(bitstr, nbits):
    """
    Epsilon is essentially the bitwise inversion of gamma, so simply
    (2**nbits - 1) - gamma
    """
    return(2**nbits - 1 - int(bitstr, 2))

def get_counter(numbers, bit):
    bits = [int(number[bit]) for number in numbers]
    return Counter(bits)
           
def bit_criterion(numbers, nbits, mode="oxygen"):
    numbers = numbers.copy()
    for bit in range(nbits):
        drop = set()
        counter = get_counter(numbers, bit)
        equal_counts = (counter[0] == counter[1])
        if mode == "oxygen":
            modeval = int(counter[1] >= counter[0])
        else:
            modeval = int(counter[0] > counter[1])
        for i, num in enumerate(numbers):
            if int(num[bit]) != modeval:
                drop.add(i)
            # Reverse such that pop does not change the meaning of an index
        for i in sorted(drop, reverse=True):
            numbers.pop(i)
            if len(numbers) == 1:
                return(int(numbers[0], 2))


if __name__ == "__main__":
    with open("day03/input.txt", "r") as f:
        lines = f.readlines()
        nbits = len(lines[0].strip())
        numbers = [l.strip() for l in lines]

        mode_bits = []
        for bit in range(nbits):
            mode_bits.append(get_counter(numbers, bit).most_common(1)[0][0])
        bitstr = "".join(map(str, mode_bits))
        print(f"Part 1: {gamma(bitstr)*epsilon(bitstr, nbits)}")

        print(f"Part 2: {bit_criterion(numbers, nbits, mode='oxygen')*bit_criterion(numbers, nbits, mode='co2')}")
