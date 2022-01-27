from src.excel_compare.file_comparison import compare_two_files

file1 = "tests/Vehicle_Motion_Manager_Vers1.xlsx"
file2 = "tests/Vehicle_Motion_Manager_Vers2.xlsx"


def test_comparison():
    compare_two_files(file1, file2)
