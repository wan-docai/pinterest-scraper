import os
import pandas as pd
import argparse

def edit_csv_to_image_ID(df_input, df_image_ID):
    file = pd.read_csv(df_input, delimiter = ',')
    newlist = file.iloc[:, 0].tolist()

    newitem = []
    for item in newlist:
        newitem.append(item.split('/'))

    image_ID = []
    for item in newitem:
        for i, n in enumerate(item):
            if i // 2 == 1:
    #         print(i)
                image_ID.append(n)

    df_image_ID = pd.DataFrame(image_ID)
    df_image_ID.to_csv(args.df_image_ID, header = None, index = False)
    return df_image_ID

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--df-input',
        required=True,
        type=str,
        help='file to edit'
    )

    parser.add_argument(
        '--df-image-ID',
        required=True,
        type=str,
        help='file to export'
    )

    args = parser.parse_args()

    edit_csv_to_image_ID(args.df_input, args.df_image_ID)




# file = pd.read_csv('unhealthy-random-image-names.csv', delimiter = ',')
#
# newlist = file.iloc[:, 0].tolist()
#
# newitem = []
# for item in newlist:
#     newitem.append(item.split('/'))
#
# image_ID = []
# for item in newitem:
#     for i, n in enumerate(item):
#         if i // 2 == 1:
# #         print(i)
#             image_ID.append(n)
#
# df_image_ID = pd.DataFrame(image_ID)
