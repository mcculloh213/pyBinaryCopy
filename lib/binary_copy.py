__author__ = "H.D. 'Chip' McCullough IV"

import os
out_loc = "../data/recv"
err_loc = "../data/err"


def copy(f_in):
    filename = os.path.split(f_in)[1]                        # Separate the filename from the dirpath
    (prefix, sep, suffix) = filename.rpartition('.')         # Separate the file name, separator, and file extension
    f_out = os.path.join(out_loc, "bin_" + prefix + ".txt")  # Set output file
    err = os.path.join(err_loc, "bin_" + prefix + ".txt")    # Set error log

    o = open(f_out, 'w')                                     # Open the output file in write mode
    try:
        with open(f_in, 'rb') as f:                          # Open the input file in binary read mode
            word = f.read(2)                                 # Read one word (2 bytes) from the binary file
            o.write(word)                                    # Write the binary to the new file

        f.close()                                            # Close input file
    except Exception as e:
        er = open(err, 'w')                                  # Open error log
        er.write("{0}".format(e))                            # Write error to error log
        er.close()                                           # Close error log
    o.close()                                                # Close output file

copy('../data/sample.txt')
