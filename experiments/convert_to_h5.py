import h5py
import cv2
import glob

# 1. Prepare image paths
image_paths = glob.glob('C:\\Users\\jfr11\\Downloads\\val\\val\\*.jpg') # replace with your image paths
img_height, img_width = 128, 128 # Define standard size
i = 0
# 2. Create HDF5 file
with h5py.File('dataset.h5', 'w') as hdf:
    # Create dataset for images and labels
    dset = hdf.create_dataset('images', (len(image_paths), img_height, img_width, 3), dtype='uint8')

    for i, img_path in enumerate(image_paths):
        # 3. Read and resize image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_height, img_width))
        # 4. Save to HDF5
        dset[i] = img

f = h5py.File('dataset.h5', 'r')
dset = f['images']
from matplotlib import pyplot as plt
plt.imshow(dset[6], interpolation='nearest')
plt.show()
f.close()
