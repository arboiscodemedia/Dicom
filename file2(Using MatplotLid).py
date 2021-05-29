import pydicom as dicom
import matplotlib.pyplot as plt

path = "./img/D0006.dcm"
x=dicom.dcmread(path)
plt.imshow(x.pixel_array,cmap=plt.cm.gray)
plt.show()