import glob

read_files = glob.glob("*.txt")

# modify image path and output file name when use
with open("result.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
