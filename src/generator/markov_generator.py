from collections import defaultdict
import random

class MarkovPasswordGenerator:
    def __init__(self, order=2):
        self.order = order
        self.transitions = {}  # {state: {next_char: count}}
        self.probabilities = {}  # {state: {next_char: probability}}
        self.start_token = "^" * order  # "^^" for order 2
        
    #load passwords and train model
    def train(self, password_file_path, max_passwords=None):
        passwords = self._load_passwords(password_file_path, max_passwords)
        self._build_transitions(passwords)
        self._normalize_probabilities()
        
    #read passwords from file
    def _load_passwords(self, filepath, max_count):
        passwords = []
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                pwd = line.strip()
                if pwd:
                    passwords.append(pwd)
                    if max_count and len(passwords) >= max_count:
                        break
        return passwords

    #builds transition counts from training passwords
    def _build_transitions(self, passwords):
        for password in passwords:
            padded_pwd = self.start_token + password
        
            for i in range(len(padded_pwd) - self.order):
                state = padded_pwd[i:i + self.order]
                next_char = padded_pwd[i + self.order]
            
                if state not in self.transitions:
                    self.transitions[state] = defaultdict(int)
            
                self.transitions[state][next_char] += 1
        padded_pwd = self.start_token + password + "$"  # Add end token

    #converts counts to probabilities
    def _normalize_probabilities(self):
        for state, next_chars in self.transitions.items():
            total = sum(next_chars.values())
            self.probabilities[state] = {}
            for char, count in next_chars.items():
                self.probabilities[state][char] = count / total

    #generate a password using the Markov model
    def generate_password(self, min_length=8, max_length=16, start_state=None):    
        if start_state is None:
            current_state = self.start_token
        else:
            current_state = start_state
        
        password = ""       
        while len(password) < max_length:
            if current_state not in self.probabilities:
                break  # no known transitions stop generation           
            next_chars = list(self.probabilities[current_state].keys())
            probabilities = list(self.probabilities[current_state].values())            
            next_char = random.choices(next_chars, weights=probabilities, k=1)[0]            
            if next_char == "$" and len(password) >= min_length:
                break  # stop if end token reached and min length met            
            password += next_char
            current_state = current_state[1:] + next_char        
        return password

if __name__ == "__main__":
    gen = MarkovPasswordGenerator(order=2)
    
    #train on a subset of rockyou.txt for testing
    print("training ")
    gen.train('data/markov/rockyou.txt')
    
    #print stats
    print(f"\ntraining complete.")
    print(f"number of unique states: {len(gen.transitions)}")
    print(f"number of unique probability states: {len(gen.probabilities)}")
    
    #show some sample transitions
    print("\n--- sample transitions ---")
    interesting_states = ['^^', 'pa', '12', 'lo', 'ss']
    
    for state in interesting_states:
        if state in gen.probabilities:
            print(f"\nstate '{state}':")
            #show top 5 next characters
            sorted_chars = sorted(gen.probabilities[state].items(), 
                                 key=lambda x: x[1], reverse=True)[:5]
            for char, prob in sorted_chars:
                print(f"  '{char}': {prob:.3f}")
        else:
            print(f"\nstate '{state}': not found in training data")


    print("\n--- generated passwords ---")
    for i in range(20):
        pwd = gen.generate_password(min_length=8, max_length=16)
        print(f"{i+1}. {pwd} (length: {len(pwd)})")
    
    print("\nshorter passwords (6-10 chars):")
    for i in range(10):
        pwd = gen.generate_password(min_length=6, max_length=10)
        print(f"{i+1}. {pwd}")
    
    print("\nlonger passwords (12-20 chars):")
    for i in range(10):
        pwd = gen.generate_password(min_length=12, max_length=20)
        print(f"{i+1}. {pwd}")