import pandas as pd
import random
import csv
import argparse
from sklearn.model_selection import train_test_split

def sample_images(filename, test, train):
    file = pd.read_csv(filename, header = None, delimiter = ',')

    train, test = train_test_split(file, test_size=0.005)

    test.to_csv(args.output_sample_file, index = False, header = None)
    train.to_csv(args.output_remaining_file, index = False, header = None)

    return test, train

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pinterest image sampler')

    parser.add_argument(
        '--filename',
        required=True,
        type=str,
        help='file containing images to sample'
    )

    parser.add_argument(
        '--output-sample-file',
        required=True,
        type=str,
        help='file name for output sample file'
    )

    parser.add_argument(
        '--output-remaining-file',
        required=True,
        type=str,
        help='file name for output remaining file'
    )

    args = parser.parse_args()

    sample_images(args.filename, args.output_sample_file, args.output_remaining_file)


    # file = pd.read_csv('unhealthy-labels.csv', delimiter = ',')
    #
    # n = len(file)
    # sample = 1000
    # skip = sorted(random.sample(range(n), n-sample))
    # df_sample = pd.read_csv('unhealthy-labels.csv', skiprows = skip)
    #
    # df_sample.to_csv('pinterest-unhealthy-labels-random-1000.csv')
