from pprint import pprint
import csv


with open("source.txt", "r") as fp:
    lines = fp.readlines()

translations = []
for line in lines:
    if line.startswith("=="):
        cur_place = line.replace("==", "").replace("\n", "").replace("[[", "").replace("]]", "")
    else:
        if line.startswith("*German:"):
            german_translation = line.replace("*German: ", "").replace("''", "").replace("\n", "")
            translations.append({"English": cur_place, "German": german_translation})
        elif line.startswith("*German"):  # source file says in this case german is same as english
            translations.append({"English": cur_place, "German": cur_place})


with open("translations.csv", "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["English", "German"])
    writer.writeheader()

    for data in translations:
        writer.writerow(data)

pprint(translations)
