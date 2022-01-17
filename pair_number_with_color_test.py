from prettytable import PrettyTable
import unittest
import get_pair_number_with_color
import get_color_coding_manual

class StatsTest(unittest.TestCase):
    def test_pair_to_number(self):
        pair_number = get_pair_number_with_color.get_pair_number_from_color("White", "Brown")
        assert (pair_number == 4)

    def test_number_to_pair(self):
        pair_number = 12
        major_color, minor_color = get_pair_number_with_color.get_color_from_pair_number(pair_number)
        assert (major_color == "Black" )
        assert (minor_color == "Orange")

    def test_color_coding_manual(self, pair_number=5):
        color_coding_manual = get_color_coding_manual.get_color_coding_manual()  # Complete manual
        pair_number_color_coding_manual = color_coding_manual.get_string\
            (border=False, header=False, fields=["Pair number", "Major color", "Minor color"],
             start=pair_number - 1, end=pair_number).strip()  # Strip the color coding manual for one value which will be tested
        known_color_coding_manual = PrettyTable(["Pair number", "Major color", "Minor color"])
        known_color_coding_manual.add_row([pair_number, "White", "Slate"])  # Building own table
        known_color_coding_manual_test = known_color_coding_manual.get_string\
            (border=False, header=False, fields=["Pair number", "Major color", "Minor color"]).strip()  # Value to be asserted, any value can be passed on from 1 to 25
        assert (known_color_coding_manual_test == pair_number_color_coding_manual)

if __name__ == "__main__":
    unittest.main()