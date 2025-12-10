# student_scores.py
def read_scores(path):
    with open(path, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]

def stats(scores):
    return {
        "count": len(scores),
        "min": min(scores),
        "max": max(scores),
        "avg": sum(scores)/len(scores)
    }

if __name__ == "__main__":
    with open("scores.txt", "w") as f:
        f.write("
".join(map(str, [78,82,91,60,55])))
    s = read_scores("scores.txt")
    print(stats(s))
