# csv_reader.py
import csv

def read_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for r in reader:
            rows.append(r)
    return rows

if __name__ == "__main__":
    sample = [["name","score"],["Aman","78"],["Rita","82"]]
    with open("sample.csv","w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(sample)
    print(read_csv("sample.csv"))
