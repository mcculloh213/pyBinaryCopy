__author__ = "H.D. 'Chip' McCullough IV"

import binascii
import os
out_loc = "./data/recv"
err_loc = "./data/err"


def copy(f_in):
    filename = os.path.split(f_in)[1]                        # Separate the filename from the dirpath
    (prefix, sep, suffix) = filename.rpartition('.')         # Separate the file name, separator, and file extension
    f_out = os.path.join(out_loc, "bin_" + prefix + ".txt")  # Set output file
    err = os.path.join(err_loc, "bin_" + prefix + ".err")    # Set error log

    o = open(f_out, 'wb')                                    # Open the output file in write mode
    try:
        with open(f_in, 'rb', 0) as f:                       # Open the input file in binary read mode
            while True:
                line = f.read(1000)                          # Read 1000 bytes of a line in the binary file
                if not line:                                 # If the line is empty
                    break                                    # EOF
                hexi = binascii.hexlify(line)                # Convert the line into hex
                binary = bin(int(hexi, 16))                  # Convert the line into decimal --> binary
                o.write(bytes(binary) + bytes('\n'))         # Write the binary word to the new file

        f.close()                                            # Close input file
    except IOError as e:
        er = open(err, 'w')                                  # Open error log
        er.write("IOError: {0}".format(e))                   # Write error to error log
        er.close()                                           # Close error log
    except TypeError as e:
        er = open(err, 'w')                                  # Open error log
        er.write("TypeError: {0}".format(e))                 # Write error to error log
        er.close()                                           # Close error log
    except Exception as e:
        er = open(err, 'w')                                  # Open error log
        er.write("Exception: {0}".format(e))                 # Write error to error log
        er.close()                                           # Close error log
    o.close()                                                # Close output file
