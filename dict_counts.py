# dict_counts.py
words = ["apple","banana","apple","orange","banana","apple"]
cnt={}
for w in words:
    cnt[w]=cnt.get(w,0)+1
print(cnt)
