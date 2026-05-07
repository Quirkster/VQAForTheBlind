# VQAForTheBlind
Supporting Visual Question answering for the Blind


#running the notebook in Zaratan
Set up a venv
It is recommended that you do this in the scratch directory
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
