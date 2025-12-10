def read_scores(path):
    with open(path, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]

def stats(scores):
    return {
        "count": len(scores),
        "min": min(scores),
        "max": max(scores),
        "avg": sum(scores) / len(scores)
    }

if __name__ == "__main__":
    # This writes REAL newlines automatically
    scores = [78, 82, 91, 60, 55]
    with open("scores.txt", "w") as f:
        for s in scores:
            f.write(f"{s}\n")

    s = read_scores("scores.txt")
    print(stats(s))
