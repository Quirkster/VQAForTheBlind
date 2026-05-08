# VQAForTheBlind
Supporting Visual Question answering for the Blind


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
You can download the pre-trained model using the hugging face command line(this is optional, but speeds up the training)


```huggingface-cli download Qwen/Qwen2-VL-7B-Instruct --cache-dir ~/scratch/hf-cache```

Our pretrained weights are in the provided zip file.

## Downloading the dataset
[Dataset](https://vizwiz.org/tasks-and-datasets/vqa/)


Note that the images and annotations are contained in separate download links.

## creating an h5 file and cropping the images
TODO

