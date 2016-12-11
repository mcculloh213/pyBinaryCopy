__author__ = "H.D. 'Chip' McCullough IV"


def stuff(sequence, bit, limit):
    """
    Bit-Stuffing algorithm
    :param sequence: binary sequence
    :type sequence: str
    :param bit: stuffing bit
    :type bit: int
    :param limit: sequence limit
    :type limit: int
    :return: Bit-stuffed sequence
    """
    count = 0                                                        # Initialize count
    s = ''
    for b in sequence:                                               # Iterate through the sequence
        if count == 0:
            if b == str(int(not bit)):
                count += 1                                           # Increment count
        else:                                                        # Count > 0
            if count < limit:                                        # Count < limit
                if b == str(int(not bit)):
                    count += 1                                       # Increment count
                else:
                    count = 0                                        # Reset count
            else:                                                    # Count == limit
                s += str(bit)                                        # Stuff bit
                count = 1                                            # Set count
        s += b
    return s
