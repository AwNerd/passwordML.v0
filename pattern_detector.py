def detect_sequential_patterns(password):
    patterns = []
    
    for i in range(len(password) - 2):
        char1, char2, char3 = password[i:i+3]
        
        if ord(char2) == ord(char1) + 1 and ord(char3) == ord(char2) + 1:
            pattern = char1 + char2 + char3
            patterns.append(('sequential_asc', pattern, i))
        
        elif ord(char2) == ord(char1) - 1 and ord(char3) == ord(char2) - 1:
            pattern = char1 + char2 + char3
            patterns.append(('sequential_desc', pattern, i))
    
    return patterns


def detect_repeated_patterns(password):
    patterns = []
    
    i = 0
    while i < len(password):
        char = password[i]
        count = 1
        
        # Count consecutive occurrences
        while i + count < len(password) and password[i + count] == char:
            count += 1
        
        # If 3+ repeats, it's a pattern
        if count >= 3:
            patterns.append(('repeated', char * count, i))
        
        i += count
    
    return patterns


def detect_keyboard_patterns(password):
    keyboard_patterns = [
        'qwerty', 'asdfgh', 'zxcvbn',  
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm', 
        'qazwsx', 'wsxedc',  
        '1234567890', '!@#$%^&*()',  
    ]
    
    patterns = []
    password_lower = password.lower()
    
    for kb_pattern in keyboard_patterns:
        for length in range(3, len(kb_pattern) + 1):
            for start in range(len(kb_pattern) - length + 1):
                substr = kb_pattern[start:start + length]
                
                if substr in password_lower:
                    idx = password_lower.index(substr)
                    patterns.append(('keyboard', password[idx:idx+length], idx))
    
    return patterns


def detect_common_substitutions(password):
    substitution_map = {
        '@': 'a', '4': 'a',
        '3': 'e', '€': 'e',
        '1': 'i', '!': 'i',
        '0': 'o',
        '$': 's', '5': 's',
        '7': 't',
    }
    
    substitutions = []
    
    for i, char in enumerate(password):
        if char in substitution_map:
            original = substitution_map[char]
            substitutions.append(('substitution', f"{char}→{original}", i))
    
    return substitutions


def analyze_patterns(password):
    sequential = detect_sequential_patterns(password)
    repeated = detect_repeated_patterns(password)
    keyboard = detect_keyboard_patterns(password)
    substitutions = detect_common_substitutions(password)
    
    all_patterns = sequential + repeated + keyboard + substitutions
    
    return {
        'sequential_patterns': sequential,
        'repeated_patterns': repeated,
        'keyboard_patterns': keyboard,
        'substitutions': substitutions,
        'total_patterns': len(all_patterns),
        'has_patterns': len(all_patterns) > 0
    }


if __name__ == "__main__":
    test_passwords = [
        "abc123",        
        "password111",   
        "qwerty",        
        "P@ssw0rd",      
        "aB3$xY9#"       
    ]
    
    for pwd in test_passwords:
        print(f"\n{'='*50}")
        print(f"Password: '{pwd}'")
        print(f"{'='*50}")
        
        result = analyze_patterns(pwd)
        
        print(f"Total Patterns Found: {result['total_patterns']}")
        
        if result['sequential_patterns']:
            print(f"Sequential: {result['sequential_patterns']}")
        
        if result['repeated_patterns']:
            print(f"Repeated: {result['repeated_patterns']}")
        
        if result['keyboard_patterns']:
            print(f"Keyboard: {result['keyboard_patterns']}")
        
        if result['substitutions']:
            print(f"Substitutions: {result['substitutions']}")
        
        if not result['has_patterns']:
            print("✓ No obvious patterns detected!")