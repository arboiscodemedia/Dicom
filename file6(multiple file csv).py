import pydicom as dicom
import os
import csv

data_dir= "./img"
patients = os.listdir(data_dir)
with open('file.csv','w') as myfile:
    writer = csv.writer(myfile)
    writer.writerow("Group Elem Description VR Value".split())
    for patient in patients:
        if patient.lower().endswith('.dcm'):
            dm = dicom.dcmread(os.path.join(data_dir,patient))
            for elem in dm:
                writer.writerow([
                    f"{elem.tag.group:04x}", f"{elem.tag.element:04x}",
                    elem.description(),elem.VR,str(elem.value)
                ])
