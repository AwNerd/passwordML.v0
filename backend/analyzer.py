

#this function checks if a password contains different character types e.g. lowercase, uppercase, digits, special characters
def count_character_types(password):
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for i in password:
        if i.islower():
            has_lowercase = True
        if i.isupper():
            has_uppercase = True
        if i.isdigit():
            has_digit = True
        if not i.isalnum():
            has_special = True

    return {
    'lowercase': has_lowercase,
    'uppercase': has_uppercase,
    'digit': has_digit,
    'special': has_special
    }


result = count_character_types("Hello123!")
print(result)

# At bottom of analyzer.py
if __name__ == "__main__":
    # Test your function
    result = count_character_types("Hello123!")
    print(result)
    # Should show which types are present
