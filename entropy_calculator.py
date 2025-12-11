import math

def calculate_pool_size(password):

    hasUpper = False
    hasLower = False
    hasDigit = False
    hasSpecial = False

    for char in password:
        if char.islower():
            hasLower = True
        elif char.isupper():
            hasUpper = True
        elif char.isdigit():
            hasDigit = True
        else:
            hasSpecial = True
    
    poolSize = 0
    if hasLower:
        poolSize += 26
    if hasUpper:
        poolSize += 26
    if hasDigit:
        poolSize += 10
    if hasSpecial:
        poolSize += 32
    return poolSize

def calculate_entropy(password):
    poolSize = calculate_pool_size(password)
    length = len(password)
    entropy = length * math.log2(poolSize)
    return entropy

if __name__ == "__main__":
    password = input("Enter the password: ")
    poolSize = calculate_pool_size(password)
    entropy = calculate_entropy(password, poolSize)
    print(f"Password Entropy: {entropy:.2f} bits")
