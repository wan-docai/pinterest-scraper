import pandas as pd
import random
import csv
import argparse

def sample_images(filename, sample_n, df_output_file):
    file = pd.read_csv(filename, delimiter = ',')

    n = len(file)
    sample_n = sample_n
    print(sample_n)

    skip = sorted(random.sample(range(n), n-sample_n))
    df_output_file = pd.read_csv(filename, skiprows = skip)
    df_output_file.to_csv(args.output_file)

    return df_output_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pinterest image sampler')

    parser.add_argument(
        '--filename',
        required=True,
        type=str,
        help='file containing images to sample'
    )

    parser.add_argument(
        '--sample-n',
        required=True,
        type=int,
        help='Number to sample'
    )

    parser.add_argument(
        '--output-file',
        required=True,
        type=str,
        help='file name for output file'
    )

    args = parser.parse_args()

    sample_images(args.filename, args.sample_n, args.output_file)



    # file = pd.read_csv('unhealthy-labels.csv', delimiter = ',')
    #
    # n = len(file)
    # sample = 1000
    # skip = sorted(random.sample(range(n), n-sample))
    # df_sample = pd.read_csv('unhealthy-labels.csv', skiprows = skip)
    #
    # df_sample.to_csv('pinterest-unhealthy-labels-random-1000.csv')
