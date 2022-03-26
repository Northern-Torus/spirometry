# import pyreadstat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
class Dataset:
  def __init__(self, data_path):
    self.data_path = data_path
  
  def clean_dataset(self, dataset):
    # Fill na db values with 0
    ds_clean = dataset.fillna(0);


    return ds_clean;

  def load_dataset(self):
    dataset = pd.read_sas(self.data_path)  # ./data/SPX_E.XPT
    return dataset;

  def build_dataset(self):
    print("Dataset built")
    ds = self.clean_dataset(self.load_dataset())
    print(ds);
    
    return ds
    
