import os
from argparse import ArgumentParser
from data import Dataset

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    parser = ArgumentParser()
    home_dir = os.getcwd()
    # FIXME
    # Arguments users used when running command lines
    parser.add_argument("--logdir", default="logs")
    parser.add_argument("--batch-size", default=64, type=int)
    parser.add_argument("--epochs", default=1000, type=int)
    parser.add_argument(
        "--data-path", default='data/SPX_E.XPT', type=str)

    args = parser.parse_args()
    # print arguments
    for i, arg in enumerate(vars(args)):
      print('{}. {}: {}'.format(i, arg, vars(args)[arg]))
    print('===========================')

    
    # Project Description
    print('---------------------------------------------------------------------')
    print('Training ${name} model with hyper-params:') # FIXME
    print('===========================')
    
    # Prepair dataset
    dataset = Dataset(args.data_path)
    ds = dataset.build_dataset()

    # FIXME
    # Do Prediction


# !python train.py --data-path ./data/SPX_E.XPT
