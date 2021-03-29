# alworldgen.py
# Cepheus Light World Generator by Omer Golan-Joel
# This is open source code, feel free to use it for any purpose
# For any questions, contact me at golan2072@gmail.com

# Import modules
import stellagama
import worldgenlib
import openpyxl
from openpyxl.styles import Font
import json
import csv


# Functions
def sector_generator(maxrow, maxcolumn):
    sector_name = stellagama.savefile("sec")
    density = input("Density from 0 to 100: ")
    output = open(sector_name, "w")
    output.write(f"{'Hex': <{5}}{'Name': <{13}}{'UWP': <{10}}{'Remarks': <{28}}{'{Ix}': <{6}}{'(Ex)': <{8}}{'[Cx]': <{7}}{'N': <{2}}{'B': <{3}}{'Z': <{2}}{'PBG': <{4}}{'W': <{3}}{'A': <{3}}{'Stellar': <{22}}\n")
    output.write("---- ------------ --------- --------------------------- ----- ------- ------ - -- - --- -- -- ----------------------\n")
    for column in range(1, maxcolumn + 1):
        for row in range(1, maxrow + 1):
            if stellagama.dice(1, 100) >= int(density):
                if row <= 9:
                    row_location = "0%i" % row
                elif row >= 10:
                    row_location = "%i" % row
                if column <= 9:
                    column_location = "0%i" % column
                elif column >= 10:
                    column_location = "%i" % column
                world_hex = column_location + row_location
                world = worldgenlib.World(world_hex)
                world_string = world.get_world_row() + "\r"
                output.write(world_string)
            else:
                pass
    output.close()


if __name__ == "__main__":
    sector_generator(40, 32)
