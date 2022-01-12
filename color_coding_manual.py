from prettytable import PrettyTable
import get_pair_number_and_color


def color_coding_manual():
    color_coding_reference_manual = PrettyTable(["Pair number", "Major color", "Minor color"])
    for pair_number in range(1, 26):
        major_color, minor_color = get_pair_number_and_color.get_color_from_pair_number(pair_number)
        color_coding_reference_manual.add_row([pair_number, major_color, minor_color])
    print(color_coding_reference_manual)
    return color_coding_reference_manual


if __name__ == "__main__":
    color_coding_manual()
