# program to convert strings of '0's and '1's into actual 0s and 1s
# originally an assignment in C, here is the analogue of that program written in python!


from Header import *


def read_til(terminating_char):
    """Input, handled the RIGHT way."""
    string = ""
    c = ""
    while c != terminating_char:
        string = string + c
        c = sys.stdin.read(1)
    return string


def get_input(prompt="Gimme string!    "):
    """Similar to:
    input()
    only better!"""
    sys.stdout.write(prompt)
    string = read_til(TERMINATING_CHAR)
    # verify input is of the right form:
    if len(string) % 8 != 0:
        sys.stdout.write("Length must be divisible by 8\n")
        # retry:
        return get_input()
    else:
        return string


def write_raw_output(integer_array):
    """Iteratively output raw binary data, one int at a time."""
    for integer in integer_array:
        sys.stdout.write(chr(integer))
        # print(integer)
    # sys.stdout.write(EOF)  # needed? cause errors?


def debug_out(iterable, message=None):
    """Outputs any iterable to stderr for debugging
    or informational purposes."""
    if message is not None:
        sys.stderr.write(message)
    for item in iterable:
        sys.stderr.write(str(item) + '\n')


def chars_to_bits(char_array):
    """Converts individual characters into corresponding
    single-digit numbers, namely 1s and 0s for our purposes."""
    bit_array = []
    for char in char_array:
        # append each number onto the array to be processed later
        bit_array.append(ord(char) - 48)  # ord() returns the Unicode index of the character. '0' is the 48th.
    return bit_array


def bits_to_byte(bit_array):
    """Takes a chunk of numbers representing bits and puts them
    into a single number composed of those bits. If given 8
    numbers, it will return a byte"""
    integer = 0
    # fake bit shifting:
    # for place in range(len(bit_array)):
    #     integer += 2**place * bit_array[7-place]
    # real bit shifting:
    for bit in bit_array:
        integer = integer << 1
        integer = integer + bit
    return integer


def convert():
    """The driver function of this program."""
    string = get_input()
    raw_binary = []
    for i in range(int(len(string)/8)):
        byte = bits_to_byte(chars_to_bits(string[i*8:i*8+8]))
        raw_binary.append(byte)
    write_raw_output(raw_binary)
    debug_out(raw_binary, "\nThe converter returned:\n")
    return SUCCESS


if __name__ == "__main__":
    sys.exit(convert())  # run convert() and exit with whatever code it returns
