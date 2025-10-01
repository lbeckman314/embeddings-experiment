with open("emoji2vec.txt", encoding="utf-8") as infile, \
     open("vectors.tsv", "w", encoding="utf-8") as vecfile, \
     open("metadata.tsv", "w", encoding="utf-8") as metafile:
    first = True
    for line in infile:
        if first:
            first = False
            continue  # Skip header
        parts = line.strip().split(" ")
        if len(parts) < 2:
            continue  # Skip malformed lines
        emoji = parts[0]
        vector = parts[1:]
        vecfile.write("\t".join(vector) + "\n")
        metafile.write(emoji + "\n")
