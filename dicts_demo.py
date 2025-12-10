# dicts_demo.py
d = {"a":1, "b":2}
d["c"] = 3
for k,v in d.items():
    print(k, v)
print("keys:", list(d.keys()))
