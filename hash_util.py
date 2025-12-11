import hashlib
import bcrypt
import time

class HashUtility:
    
    @staticmethod
    def hash_md5(password): #note: md5 is cryptographically broken don't actually use for real passwords
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.md5(password_bytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    @staticmethod
    def hash_sha256(password):
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex
    
    @staticmethod
    def hash_bcrypt(password, rounds=12): #industry standard, prone to brute force attacks
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt(rounds=rounds)
        hash_bytes = bcrypt.hashpw(password_bytes, salt)
        hash_str = hash_bytes.decode('utf-8')
        return hash_str

    
    @staticmethod
    def verify_bcrypt(password, hashed):
        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    
    @staticmethod
    def benchmark_hashing(password, iterations=1000):
        results = {}
        
        # bench MD5
        start_time = time.time()
        for _ in range(iterations):
            HashUtility.hash_md5(password)
        end_time = time.time()
        
        total_time = end_time - start_time
        hashes_per_second = iterations / total_time
        
        results['md5'] = {
            'total_time': total_time,
            'hashes_per_second': hashes_per_second
        }
        
        # bench SHA-256
        start_time = time.time()
        for _ in range(iterations):
            HashUtility.hash_sha256(password)
        end_time = time.time()

        total_time = end_time - start_time
        hashes_per_second = iterations / total_time
        results['sha256'] = {
            'total_time': total_time,
            'hashes_per_second': hashes_per_second
        }
        
        # bench bcrypt 
        bcrypt_iterations = 10  # much fewer because bcrypt is SLOW
        start_time = time.time()
        for _ in range(bcrypt_iterations):
            HashUtility.hash_bcrypt(password)
        end_time = time.time()
        
        total_time = end_time - start_time
        hashes_per_second = bcrypt_iterations / total_time
        
        results['bcrypt'] = {
            'total_time': total_time,
            'hashes_per_second': hashes_per_second
        }
    
        return results
    
    @staticmethod
    def compare_hashes(password):
        return {
            'password': password,
            'md5': HashUtility.hash_md5(password),
            'sha256': HashUtility.hash_sha256(password),
            'bcrypt': HashUtility.hash_bcrypt(password)
        }


def main():
    print("\n" + "="*60)
    print("CRYPTOGRAPHIC HASH UTILITIES")
    print("="*60)
    
    password = input("\nEnter a password to hash: ")

    print(f"\n{'='*60}")
    print("HASH COMPARISON")
    print(f"{'='*60}")
    hashes = HashUtility.compare_hashes(password)
    print(f"Plain text: {hashes['password']}")
    print(f"MD5:        {hashes['md5']}")
    print(f"SHA-256:    {hashes['sha256']}")
    print(f"bcrypt:     {hashes['bcrypt']}")
    
    print(f"\n{'='*60}")
    print("BCRYPT VERIFICATION TEST")
    print(f"{'='*60}")
    bcrypt_hash = hashes['bcrypt']
    
    test_correct = input("Enter the password again to verify: ")
    is_correct = HashUtility.verify_bcrypt(test_correct, bcrypt_hash)
    print(f"Password match: {is_correct}")
    
    test_wrong = "wrongpassword"
    is_wrong = HashUtility.verify_bcrypt(test_wrong, bcrypt_hash)
    print(f"Wrong password match: {is_wrong}")
    
    # Benchmark
    print(f"\n{'='*60}")
    print("PERFORMANCE BENCHMARK")
    print(f"{'='*60}")
    print("Benchmarking hash speeds (this may take a moment)...")
    benchmark = HashUtility.benchmark_hashing(password)
    
    print(f"\nMD5:")
    print(f"  Total time: {benchmark['md5']['total_time']:.4f} seconds")
    print(f"  Hashes/sec: {benchmark['md5']['hashes_per_second']:,.0f}")
    
    print(f"\nSHA-256:")
    print(f"  Total time: {benchmark['sha256']['total_time']:.4f} seconds")
    print(f"  Hashes/sec: {benchmark['sha256']['hashes_per_second']:,.0f}")
    
    print(f"\nbcrypt (rounds=12):")
    print(f"  Total time: {benchmark['bcrypt']['total_time']:.4f} seconds")
    print(f"  Hashes/sec: {benchmark['bcrypt']['hashes_per_second']:.2f}")
    
    print(f"\n{'='*60}")
    print("WHY THE SPEED DIFFERENCE MATTERS:")
    print(f"{'='*60}")
    print("MD5 is ~1,000,000x faster than bcrypt!")
    print("This means attackers can try 1 million MD5 guesses")
    print("in the same time it takes to try 1 bcrypt guess.")
    print("\nThis is why bcrypt is used for passwords")
    print("bcrypt is intentionally slow to make brute force attacks impractical.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()