import math
from entropy_calculator import calculate_entropy, calculate_pool_size
from diversity_analyzer import analyze_diversity
from pattern_detector import analyze_patterns

class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password
        self.results = {}
    
    def analyze(self):
        self.results['entropy'] = self._analyze_entropy()
        
        self.results['diversity'] = analyze_diversity(self.password)
        
        self.results['patterns'] = analyze_patterns(self.password)
        
        self.results['overall_score'] = self._calculate_overall_score()
        
        return self.results
    
    def _analyze_entropy(self):
        entropy = calculate_entropy(self.password)
        pool_size = calculate_pool_size(self.password)
        strength = self._interpret_strength(entropy)
        
        return {
            'bits': entropy,
            'pool_size': pool_size,
            'length': len(self.password),
            'strength': strength,
            'time_to_crack': self._estimate_crack_time(entropy)
        }
    
    def _interpret_strength(self, entropy_bits):
        if entropy_bits < 28:
            return {
                'rating': 'Very Weak',
                'color': 'red',
                'description': 'Crackable instantly'
            }
        elif entropy_bits < 36:
            return {
                'rating': 'Weak',
                'color': 'orange',
                'description': 'Crackable in hours'
            }
        elif entropy_bits < 60:
            return {
                'rating': 'Moderate',
                'color': 'yellow',
                'description': 'Crackable in days/weeks'
            }
        elif entropy_bits < 80:
            return {
                'rating': 'Strong',
                'color': 'lightgreen',
                'description': 'Crackable in years'
            }
        else:
            return {
                'rating': 'Very Strong',
                'color': 'green',
                'description': 'Practically uncrackable'
            }
    
    def _estimate_crack_time(self, entropy_bits):
        total_combinations = 2 ** entropy_bits
        guesses_per_second = 10_000_000_000  
        
        seconds = total_combinations / guesses_per_second
        
        if seconds < 1:
            return "< 1 second"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.1f} days"
        elif seconds < 31536000 * 100:
            return f"{seconds/31536000:.1f} years"
        else:
            return f"{seconds/31536000:.2e} years"
    
    def _calculate_overall_score(self):
        entropy_bits = self.results['entropy']['bits']
        entropy_score = min(50, (entropy_bits / 80) * 50)
        
        diversity_ratio = self.results['diversity']['diversity_score']
        diversity_score = diversity_ratio * 25
        
        pattern_count = self.results['patterns']['total_patterns']
        pattern_score = max(0, 25 - (pattern_count * 5))
        
        total_score = entropy_score + diversity_score + pattern_score
        
        return {
            'score': round(total_score, 1),
            'max_score': 100,
            'breakdown': {
                'entropy': round(entropy_score, 1),
                'diversity': round(diversity_score, 1),
                'pattern': round(pattern_score, 1)
            }
        }
    
    def print_report(self):
        if not self.results:
            self.analyze()
        
        print("\n" + "="*60)
        print(f"PASSWORD SECURITY ANALYSIS: '{self.password}'")
        print("="*60)
        
        #overall score
        score = self.results['overall_score']['score']
        print(f"\nOVERALL SCORE: {score}/100")
        print(f"   Entropy: {self.results['overall_score']['breakdown']['entropy']}/50")
        print(f"   Diversity: {self.results['overall_score']['breakdown']['diversity']}/25")
        print(f"   Pattern Score: {self.results['overall_score']['breakdown']['pattern']}/25")
        
        #entropy analysis
        print(f"\nENTROPY ANALYSIS")
        print(f"   Entropy: {self.results['entropy']['bits']:.2f} bits")
        print(f"   Character Pool Size: {self.results['entropy']['pool_size']}")
        print(f"   Length: {self.results['entropy']['length']} characters")
        print(f"   Strength: {self.results['entropy']['strength']['rating']} - {self.results['entropy']['strength']['description']}")
        print(f"   Estimated Crack Time: {self.results['entropy']['time_to_crack']}")
        
        #diversity
        print(f"\nCHARACTER DIVERSITY")
        print(f"   Diversity Score: {self.results['diversity']['diversity_score']:.2%}")
        print(f"   Unique Characters: {self.results['diversity']['unique_chars']}/{self.results['diversity']['total_chars']}")
        print(f"   Most Common: '{self.results['diversity']['most_common_char']}' (appears {self.results['diversity']['most_common_count']} times)")
        
        #pattern
        print(f"\nPATTERN DETECTION")
        patterns = self.results['patterns']
        
        if not patterns['has_patterns']:
            print("   No obvious patterns detected!")
        else:
            print(f"   {patterns['total_patterns']} pattern(s) detected:")
            
            if patterns['sequential_patterns']:
                print(f"      Sequential: {len(patterns['sequential_patterns'])} found")
                for p in patterns['sequential_patterns']:
                    print(f"        - '{p[1]}' at position {p[2]}")
            
            if patterns['repeated_patterns']:
                print(f"      Repeated: {len(patterns['repeated_patterns'])} found")
                for p in patterns['repeated_patterns']:
                    print(f"        - '{p[1]}' at position {p[2]}")
            
            if patterns['keyboard_patterns']:
                print(f"      Keyboard: {len(patterns['keyboard_patterns'])} found")
                for p in patterns['keyboard_patterns']:
                    print(f"        - '{p[1]}' at position {p[2]}")
            
            if patterns['substitutions']:
                print(f"      Substitutions: {len(patterns['substitutions'])} found")
                for p in patterns['substitutions']:
                    print(f"        - {p[1]} at position {p[2]}")
        
        #reccomendations
        print(f"\nRECOMMENDATIONS")
        self._print_recommendations()
        
        print("\n" + "="*60 + "\n")
    
    def _print_recommendations(self):
        """Generate and print recommendations based on analysis."""
        recommendations = []
        
        if self.results['entropy']['bits'] < 60:
            recommendations.append("Increase password length (aim for 12+ characters)")
            recommendations.append("Use a mix of uppercase, lowercase, numbers, and symbols")
        
        if self.results['diversity']['diversity_score'] < 0.7:
            recommendations.append("Avoid repeating characters too often")
        
        if self.results['patterns']['sequential_patterns']:
            recommendations.append("Avoid sequential characters (abc, 123)")
        
        if self.results['patterns']['repeated_patterns']:
            recommendations.append("Avoid repeated characters (aaa, 111)")
        
        if self.results['patterns']['keyboard_patterns']:
            recommendations.append("Avoid keyboard patterns (qwerty, asdf)")
        
        if self.results['patterns']['substitutions']:
            recommendations.append("Common substitutions (@=a, 3=e, 0=o) are easily guessed")
        
        if not recommendations:
            recommendations.append("✓ This is a strong password! Keep it secure.")
        
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")


def main():
    print("\n" + "="*60)
    print("PASSWORD SECURITY ANALYZER")
    print("Analyzing password strength using entropy, diversity, and patterns")
    print("="*60)
    
    while True:
        password = input("\nEnter password to analyze (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            break
        
        if not password:
            print("Please enter a password")
            continue
        
        analyzer = PasswordAnalyzer(password)
        analyzer.print_report()
        
        another = input("\nAnalyze another password? (y/n): ")
        if another.lower() != 'y':
            break


if __name__ == "__main__":
    main()