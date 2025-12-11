# diversity_analyzer.py
from collections import Counter

def calculate_character_diversity(password):
    if len(password) == 0:
        return 0.0
    
    unique_chars = len(set(password))
    total_chars = len(password)
    return unique_chars / total_chars


def detect_character_distribution(password):
    if len(password) == 0:
        return {
            'most_common_char': None,
            'most_common_count': 0,
            'frequency_distribution': {}
        }

    char_counts = Counter(password)
    
    most_common = char_counts.most_common(1)[0]
    
    return {
        'most_common_char': most_common[0],
        'most_common_count': most_common[1],
        'frequency_distribution': dict(char_counts)
    }


def analyze_diversity(password):
    diversity_score = calculate_character_diversity(password)
    distribution = detect_character_distribution(password)
    
    return {
        'diversity_score': diversity_score,
        'unique_chars': len(set(password)),
        'total_chars': len(password),
        'most_common_char': distribution['most_common_char'],
        'most_common_count': distribution['most_common_count'],
        'distribution': distribution['frequency_distribution']
    }


if __name__ == "__main__":
    test_passwords = [
        "aaaa",           
        "abcd",           
        "password",       
        "P@ssw0rd123"     
    ]
    
    for pwd in test_passwords:
        print(f"\n{'='*50}")
        print(f"Password: '{pwd}'")
        print(f"{'='*50}")
        
        result = analyze_diversity(pwd)
        
        print(f"Diversity Score: {result['diversity_score']:.2%}")
        print(f"Unique Characters: {result['unique_chars']}/{result['total_chars']}")
        print(f"Most Common Character: '{result['most_common_char']}' (appears {result['most_common_count']} times)")
        print(f"Character Distribution: {result['distribution']}")