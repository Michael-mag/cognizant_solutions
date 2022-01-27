import xml.etree.ElementTree as ET
from openpyxl import Workbook

# input_file = "/Users/michael/PycharmProjects/pythonProject15/tests/test_input/test.xml"


def driver_code(input_file: str) -> None:
    xml_tree = ET.parse(input_file)
    root = xml_tree.getroot()

    # initialize some excel work book information
    wb = Workbook()
    ws = wb.active
    ws.title = "Converted XML file data"

    # create the header row for the excel sheet
    ws.append(
        [
            "Name",
            "SenderPort",
            "ReceiverPort",
            "UUID",
        ]
    )

    xml_parser(root, ws)
    wb.save(filename="converted_xml_file.xlsx")


def xml_parser(root: ET.Element, ws: Workbook) -> None:
    for tag in root:
        name = None
        uid = None
        sender_ports = []
        receiver_ports = []

        for tag_data in tag:
            if tag_data.tag == "Name":
                name = tag_data.text
            if tag_data.tag == "UID":
                uid = tag_data.text
            if tag_data.tag == "SenderPort":
                sender_ports.append(tag_data.text)
            if tag_data.tag == "ReceiverPort":
                receiver_ports.append(tag_data.text)

        # write to excel
        ws.append([name, sender_ports[0], receiver_ports[0], uid])

        # since openpyxl only supports row-wise file writing, iterate over the length
        #   of either the receiver list or sender list, assuming for each sender there
        #   is a corresponding receiver.
        for i in range(1, len(sender_ports)):
            ws.append(["", sender_ports[i], receiver_ports[i], ""])

    return ws
