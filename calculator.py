# calculator.py
def calc(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "inf"
    return None

if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    op = input("operator (+ - * /): ")
    print("Result:", calc(a, b, op))
