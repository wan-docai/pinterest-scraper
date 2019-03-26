import glob

read_files = glob.glob("./image_url/not_food/*.txt")

# modify image path and output file name when use
with open("not_food.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
