#!/usr/bin/env python3
"""
read the drills from the soccer
 file and put in datafram
"""

import pandas as pd


def read_drills(filename):
    """Read the drills from the soccer file and put in dataframe"""
    drills = pd.read_csv(filename)
    print(drills)


if __name__ == "__main__":
    read_drills("./Full_Soccer_Drills_List.csv")
