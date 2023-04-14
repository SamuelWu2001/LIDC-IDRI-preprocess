import numpy as np 
from PIL import Image

import os
print(os.path.abspath("."))

# img_array = np.load(R'C:\Users\samue\VScode\MedicalImageSystem\LIDC-IDRI-Preprocessing\data\Image\LIDC-IDRI-0003\0003_NI003_slice002.npy')
# mask_array = np.load(R'C:\Users\samue\VScode\MedicalImageSystem\LIDC-IDRI-Preprocessing\data\Mask\LIDC-IDRI-0003\0003_MA003_slice002.npy')

img_array = np.load(R'C:\Users\samue\VScode\MedicalImageSystem\LIDC-IDRI-Preprocessing\data\Clean\Image\LIDC-IDRI-0028\0028_CN001_slice003.npy')
mask_array = np.load(R'C:\Users\samue\VScode\MedicalImageSystem\LIDC-IDRI-Preprocessing\data\Clean\Mask\LIDC-IDRI-0028\0028_CM001_slice003.npy')

img_array = (img_array-img_array.min())/((img_array.max()-img_array.min())/255.0)
img = Image.fromarray(img_array)
print(img_array)
img.show()
mask = Image.fromarray(mask_array)
mask.show()