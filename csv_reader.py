# csv_reader.py
import csv
import sys

def read_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for r in reader:
            rows.append(r)
    return rows

def scores_stats(rows):
    # expect header in row 0, numeric scores in column 1
    scores = []
    for r in rows[1:]:
        if len(r) < 2:
            continue
        try:
            scores.append(int(r[1]))
        except:
            continue
    if not scores:
        return {}
    return {"count": len(scores), "min": min(scores), "max": max(scores), "avg": sum(scores)/len(scores)}

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "sample.csv"
    rows = read_csv(path)
    print("ROWS:", rows)
    print("SCORE_STATS:", scores_stats(rows))
