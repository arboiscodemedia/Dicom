import pydicom as dicom

path="./img/D0006.dcm"
x=dicom.dcmread(path)
print(dir(x))
