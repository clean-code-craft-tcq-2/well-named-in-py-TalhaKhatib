"""
Generate complete color coding manual
"""

from prettytable import PrettyTable

import get_pair_number_with_color


def get_color_coding_manual():
    reference_color_coding_manual = PrettyTable(["Pair number", "Major color", "Minor color"])
    for pair_number in range(1, 26):
        major_color, minor_color = get_pair_number_with_color.get_color_from_pair_number(pair_number)
        reference_color_coding_manual.add_row([pair_number, major_color, minor_color])
    #print(reference_color_coding_manual)
    return reference_color_coding_manual

