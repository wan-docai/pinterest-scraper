import glob

read_files = glob.glob("./image_url/healthy/*.txt")

# modify image path and output file name when use
with open("healthy.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
