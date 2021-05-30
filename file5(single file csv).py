import csv
from os import write
import pydicom as dicom

ds =  dicom.dcmread("./img/D0001.dcm")

with open('my.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow("Group Elem Description VR Value".split())
    for elem in ds:
        writer.writerow([
            f"{elem.tag.group:04x}", f"{elem.tag.element:04x}",
            elem.description(),elem.VR,str(elem.value)
        ])