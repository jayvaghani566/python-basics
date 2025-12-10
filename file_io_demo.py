# file_io_demo.py
with open("demo.txt","w",encoding="utf-8") as f:
    f.write("line1\nline2\n")
with open("demo.txt","r",encoding="utf-8") as f:
    print(f.read())
