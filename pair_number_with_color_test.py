from prettytable import PrettyTable
import unittest

import get_pair_number_with_color
import get_color_coding_manual


class StatsTest(unittest.TestCase):
    def test_pair_to_number(self):
        """
        Testing the get_pair_number_from_color.py
        """
        pair_number = get_pair_number_with_color.get_pair_number_from_color("White", "Brown")
        expected_pair_number = 4
        assert (pair_number == expected_pair_number)


    def test_number_to_pair(self):
        """
        Testing the get_color_from_pair_number.py
        """
        pair_number = 12
        expected_major_color = "Black"
        expected_minor_color = "Orange"
        major_color, minor_color = get_pair_number_with_color.get_color_from_pair_number(pair_number)
        assert (major_color == expected_major_color)
        assert (minor_color == expected_minor_color)


    def test_color_coding_manual(self):
        """
        Testing the get_color_coding_manual.py
        """
        pair_number = 5
        color_coding_manual = get_color_coding_manual.get_color_coding_manual() #Complete manual
        pair_number_color_coding_manual = color_coding_manual.get_string \
            (border=False, header=False, fields=["Pair number", "Major color", "Minor color"],
             start=pair_number-1, end=pair_number)\
            .strip()  #Strip the color coding manual for one value which will be tested

        known_color_coding_manual = PrettyTable(["Pair number", "Major color", "Minor color"]) #Building own table
        known_color_coding_manual.add_row([pair_number, "White", "Slate"])
        known_color_coding_manual_test = known_color_coding_manual.get_string \
            (border=False, header=False, fields=["Pair number", "Major color", "Minor color"],
             # start=0, end=1
             ).strip()  #Value to be asserted, any value can be passed on from 1 to 25

        #print(known_color_coding_manual_test)
        #print(pair_number_color_coding_manual)

        assert (known_color_coding_manual_test == pair_number_color_coding_manual)

if __name__ == "__main__":
    unittest.main()

#if __name__ == "__main__":
    #test_number_to_pair(4, 'White', 'Brown')
    #test_number_to_pair(5, 'White', 'Slate')
    #test_pair_to_number('Black', 'Orange', 12)
    #test_pair_to_number('Violet', 'Slate', 25)
    #test_pair_to_number('Red', 'Orange', 7)
    #test_color_coding_manual(5, "White", "Slate")
