# palindrome.py
s = input("String: ").strip()
print("Palindrome" if s == s[::-1] else "Not palindrome")
