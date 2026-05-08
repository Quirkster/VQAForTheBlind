import h5py
import cv2
import glob
import argparse

# use --input_dir to specify the folder with all of the images
# use --output_file to name the output h5 file, default is dataset.h5
parser = argparse.ArgumentParser(description='Convert images to HDF5 format')
parser.add_argument('--input_dir', type=str, required=True, help='Directory containing input images')
parser.add_argument('--output_file', type=str, default='dataset.h5', help='Output HDF5 file name')
args = parser.parse_args()

# 1. Prepare image paths
image_paths = glob.glob(args.input_dir + '/*.jpg') # replace with your image paths
img_height, img_width = 128, 128 # Define standard size
# 2. Create HDF5 file
with h5py.File(args.output_file, 'w') as hdf:
    # Create dataset for images and labels
    dset = hdf.create_dataset('images', (len(image_paths), img_height, img_width, 3), dtype='uint8')

    for i, img_path in enumerate(image_paths):
        # 3. Read and resize image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (img_height, img_width))
        # 4. Save to HDF5
        dset[i] = img

# example to read an image from the h5 file, you can run this part separately after the conversion is done
f = h5py.File(args.output_file, 'r')
dset = f['images']
from matplotlib import pyplot as plt
plt.imshow(dset[0], interpolation='nearest') # change dset[0] to any index to view a different image
plt.show()
f.close()
