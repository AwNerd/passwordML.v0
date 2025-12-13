import time
import sys
import markovify
from memory_profiler import profile  

sys.path.append('../src/generator')
from markov_generator import MarkovPasswordGenerator

# benchmark training time
def benchmark_training(data_path, sample_size=10000):
    start = time.time()
    custom_gen = MarkovPasswordGenerator(order=2)
    custom_gen.train(data_path, max_passwords=sample_size)
    custom_time = time.time() - start
    
    # markovify (needs text format)
    start = time.time()
    with open(data_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = '\n'.join([f.readline().strip() for _ in range(sample_size)])
    markov_model = markovify.Text(text, state_size=2)
    markovify_time = time.time() - start
    
    return custom_time, markovify_time, custom_gen, markov_model

def benchmark_generation(custom_gen, markov_model, num_passwords=100):
    start = time.time()
    for _ in range(num_passwords):
        custom_gen.generate_password(min_length=8, max_length=16)
    custom_time = time.time() - start
    
    # markovify
    start = time.time()
    for _ in range(num_passwords):
        markov_model.make_short_sentence(max_chars=16, tries=100)
    markovify_time = time.time() - start
    
    return custom_time, markovify_time

def compare_output_quality(custom_gen, markov_model, num_samples=20):
    print("\noutput quality comparison:")
    print("\ncustom implementation:")
    for i in range(num_samples):
        print(f"  {custom_gen.generate_password(8, 16)}")
    
    print("\nmarkovify:")
    for i in range(num_samples):
        result = markov_model.make_short_sentence(max_chars=16, tries=100)
        print(f"  {result if result else '[failed to generate]'}")

if __name__ == "__main__":
    data_path = 'data/markov/rockyou.txt'
    
    print("markov password generator benchmark")
    print("data source: rockyou.txt\n")
    
    # training benchmark
    print("\n[training benchmark (10k passwords)")
    custom_train_time, markovify_train_time, custom_gen, markov_model = benchmark_training(data_path, 10000)
    
    print(f"  custom implementation: {custom_train_time:.3f}s")
    print(f"  markovify: {markovify_train_time:.3f}s")
    print(f"  winner: {'custom' if custom_train_time < markovify_train_time else 'markovify'} ({abs(custom_train_time - markovify_train_time):.3f}s faster)")
    
    # generation benchmark
    print("\n[generation benchmark (100 passwords)]")
    custom_gen_time, markovify_gen_time = benchmark_generation(custom_gen, markov_model, 100)
    
    print(f"  custom implementation: {custom_gen_time:.3f}s ({100/custom_gen_time:.1f} passwords/sec)")
    print(f"  markovify: {markovify_gen_time:.3f}s ({100/markovify_gen_time:.1f} passwords/sec)")
    print(f"  winner: {'Custom' if custom_gen_time < markovify_gen_time else 'markovify'}")
    
    print("\noutpput quality comparison...")
    compare_output_quality(custom_gen, markov_model, 10)
    
    print("\nsummary")
    print(f"custom implementation states: {len(custom_gen.transitions)}")