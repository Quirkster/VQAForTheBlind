# VQAForTheBlind
Training a Visual Language model to provide clear, concise answers to questions about photos taken by blind people.

# Running the notebook in Zaratan
## Set up a venv
It is recommended that you do this in the scratch directory.
```
module load python
unset PYTHONPATH
unset LD_LIBRARY_PATH
python -m venv ~/cmsc472final-venv

source ~/cmsc472final-venv/bin/activate

python -m pip install --upgrade pip ipykernel

python -m ipykernel install --user \
--name=cmsc472final-venv \
--display-name="Python (cmsc472final-venv)"

mkdir jupyter-runtime
mkdir hf-cache
mkdir pip-cache

```

## Downloading the model
You can download the pre-trained model using the hugging face command line(this is optional, but speeds up the training), if you do so, change local_files_only to true in cell 4 of CMSC472Final.ipynb


```huggingface-cli download Qwen/Qwen2-VL-7B-Instruct --cache-dir /path/to/hf-cache```

Our pretrained weights are in the provided zip file.

## Downloading the dataset
[Dataset](https://vizwiz.org/tasks-and-datasets/vqa/)


Note that the images and annotations are contained in separate download links.

## Creating an h5 file and cropping the images
Our program requires the data to be in the h5 format. Run experiments/convert_to_h5.py on both the train and validation set of images, using the argument --input_dir path_to_directory and replace path_to_directory with the path to the folder that contains all the images. You can specify the output folder name with the argument --output_file output_file_name and replace output_file_name with your desired name. The default is dataset.h5.

In order to test out our model with cropped images, use src/Object_localization.ipynb.

Store these images in the directory you will run the notebook from with the following names:
Train images: train_dataset.h5
Train cropped images: train_dataset_cropped.h5
Train annotations: train.json

Validation images: val_dataset.h5
Validation cropped images: val_dataset_cropped.h5
Validation annotations: val.json
## Training the model
The notebook with the model code is CMSC472Final.ipynb. Before running the notebook, change the path_to_directory variable in cell 3 to the path to your hf-cache. 

Running the full notebook (CMSC472final.ipynb) will:
1. Evaluate the baseline VLM on the train and val set on both cropped and uncropped images(approx 3 hours)
2. Fine tune the model(approx 6 hours)
3. Evaluate the fine-tuned model(approx 3 hours)

Runtimes listed are with a single a100 gpu.

### To evaluate without training
Run the notebook excluding cell #13, 14

### To train without evaluating
Run the notebook excluding cells #11, #15, 17


