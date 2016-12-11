import unittest
import lib.bit_stuffer as bs

__author__ = "H.D. 'Chip' McCullough IV"


class MyTestCase(unittest.TestCase):
    def test_no_stuff_zeroes(self):
        s = '0b00000'
        sp = bs.stuff(s, 0, 5)
        self.assertEqual(s, sp)

    def test_no_stuff_ones(self):
        s = '0b11111'
        sp = bs.stuff(s, 1, 5)
        self.assertEqual(s, sp)

    def test_stuff_with_zeroes_1(self):
        s = '0b111111'
        sp = bs.stuff(s, 0, 5)
        self.assertEqual('0b1111101', sp)

    def test_stuff_with_zeros_2(self):
        s = "0b0001111111111110011111001111110"
        sp = bs.stuff(s, 0, 5)
        self.assertEqual('0b00011111011111011001111100011111010', sp)

    def test_stuff_with_ones_1(self):
        s = '0b000000'
        sp = bs.stuff(s, 1, 5)
        self.assertEqual('0b0000010', sp)

    def test_stuff_with_ones_2(self):
        s = "0b1110000000000001100000110000001"
        sp = bs.stuff(s, 1, 5)
        self.assertEqual('0b11100000100000100110000011100000101', sp)

if __name__ == '__main__':
    unittest.main()
