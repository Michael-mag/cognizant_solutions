from src.xml_to_excel_converter.xml_to_xlsx import driver_code


def test_xml_converter():
    input_file = "tests/test.xml"
    driver_code(input_file)