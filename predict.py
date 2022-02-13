import os
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--batch-size", default=64, type=int)
    parser.add_argument("--epochs", default=1000, type=int)

    args = parser.parse_args()
    
    # Project Description
    print('Training ${name} model with hyper-params:') # FIXME
    print('===========================')

    # FIXME
    # Do Training

