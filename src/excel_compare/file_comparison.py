import pandas as pd
import numpy as np
from typing import Union
from pathlib import Path


def compare_two_files(file1: Union[str, Path], file2: Union[str, Path]) -> None:
    """
    :param file1: Excel file version 1
    :param file2: Excel file version 2
    :return: None
    """

    # read the excel files into pandas dataframes df1 and df2
    file1_data_frame = pd.read_excel(file1)
    file2_data_frame = pd.read_excel(file2)
    df1 = pd.DataFrame(file1_data_frame)
    df2 = pd.DataFrame(file2_data_frame)

    # for debugging purposes, use a copy of df1, named df3
    df3 = df1.copy()

    # get the locations where corresponding columns do not have the same value
    rows, columns = np.where(df1 != df2)

    # for each tuple that represents the row, and column location of the un-identical values,
    #   rewrite the value of this location in df3 in the form Vers1[Vers2]
    for entry in zip(rows, columns):
        df3.iloc[entry[0], entry[1]] = "{}[{}]".format(
            df3.iloc[entry[0], entry[1]], df2.iloc[entry[0], entry[1]]
        )

    df3 = df3.replace("nan[nan]", "")
    df3 = df3.iloc[1:, :]   # The first non-header row is blank, remove it.
    df3.to_excel("result.xlsx")


if __name__ == "__main__":
    # please run using pytest as described in readme.
    file1 = "/Users/michael/PycharmProjects/pythonProject15/tests/test_input/Vehicle_Motion_Manager_Vers1.xlsx"
    file2 = "/Users/michael/PycharmProjects/pythonProject15/tests/test_input/Vehicle_Motion_Manager_Vers2.xlsx"
    compare_two_files(file1, file2)
