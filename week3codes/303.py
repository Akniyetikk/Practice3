triplet_to_digit = {
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9",
    "ZER": "0"
}

digit_to_triplet = {v: k for k, v in triplet_to_digit.items()}

def decode_number(s):
    num_str = ""
    for i in range(0, len(s), 3):
        num_str += triplet_to_digit[s[i:i+3]]
    return int(num_str)

def encode_number(n):
    if n == 0:
        return "ZER"
    res = ""
    for digit in str(n):
        if digit == '-':
            res += "-"  
        else:
            res += digit_to_triplet[digit]
    return res

def calculate(expression):
    for op in "+-*":
        if op in expression:
            left, right = expression.split(op)
            a = decode_number(left)
            b = decode_number(right)
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            else:
                result = a * b
            return encode_number(result)

expr = input().strip()
print(calculate(expr))
