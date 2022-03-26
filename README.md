# Spirometry

## I.  Set up environment

```python
conda env create -f environment.yml

```

```sh
conda activate torus-project 
```

## II.  Set up your dataset
- Guide user how to download your data and set the data pipeline 

Data processing script:
```python
python data.py
```

## III. Training Process

Training script:

```python
python train.py --epochs ${epochs}
```