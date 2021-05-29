import pydicom as dicom
import numpy as np
from PIL import Image
import os

def convert(directory):
    im = dicom.dcmread('./img/'+directory)
    im = im.pixel_array.astype(float)
    rescaled_image = (np.maximum(im,0)/im.max()) * 255 # float pixel
    final_image = np.uint8(rescaled_image) # integers pixels
    final_image = Image.fromarray(final_image)
    return final_image


path="./img"
ct_images = os.listdir(path)
arr_filename = [x for x in ct_images if x.endswith(".dcm")]

for name in arr_filename:
    image = convert(name)
    image.save('./JPG_IMG/'+name+'.jpg')