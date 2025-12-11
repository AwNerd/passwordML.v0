# PasswordML

An ML-enhanced password security research toolkit that combines traditional cryptographic methods with machine learning to analyze password vulnerabilities and attack patterns.

> **Active Research Project** - I'm exploring the intersection of machine learning and cybersecurity

---

## Project Overview

I'm building PasswordML to investigate how machine learning and statistical models can make password cracking smarter and more efficient. This project serves as both a security research tool and my deep dive into applied ML for cybersecurity.

**What I'm focusing on:**
- Understanding common password vulnerabilities through data analysis
- Implementing traditional attack vectors (dictionary, brute force)
- Enhancing attack efficiency using Markov chains and neural networks
- Comparing ML vs. traditional methods with real metrics

---

## Research Questions I'm Exploring

- Can neural networks predict likely passwords better than traditional wordlists?
- How effective are Markov chains at generating human-like passwords?
- What patterns exist in compromised password databases?
- How does entropy calculation correlate with actual crackability?
- What's the performance tradeoff between ML inference and brute computation?

---

## My Development Roadmap

### Phase 1: Foundation (Current)
- [x] Entropy-based password strength analyzer
- [x] Character diversity detection system
- [x] Pattern recognition (sequential/repeated characters)
- [ ] Cryptographic hash utilities (MD5, SHA256, bcrypt)

### Phase 2: Traditional & Statistical Methods 
- [ ] Dictionary attack with performance metrics
- [x] Markov chain password generator (n-gram based)
- [ ] Multi-threaded brute force optimization
- [ ] Wordlist management system
- [ ] Attack success rate analytics

### Phase 3: Deep Learning Enhancement 
- [ ] Dataset preprocessing (RockYou, SecLists)
- [ ] Character-level RNN for password generation
- [ ] PassGAN-inspired GAN architecture
- [ ] Comparative benchmarking: Dictionary vs. Markov vs. Neural
- [ ] Transfer learning from breach datasets

### Phase 4: Advanced Research
- [ ] Personal-info-based password prediction
- [ ] Ensemble methods (combining multiple models)
- [ ] Real-time attack visualization
- [ ] Automated report generation with statistics

---

## Tech Stack

**What I'm using now:**
- **Python 3.x** - Core development language
- **hashlib** - Cryptographic hashing
- **collections** - Efficient data structures (defaultdict for Markov chains)
- **Custom algorithms** - Entropy calculation, pattern detection

**What I'm planning to integrate:**
- **PyTorch/TensorFlow** - Neural network training
- **NumPy/Pandas** - Dataset analysis
- **Multiprocessing** - Performance optimization
- **Matplotlib/Seaborn** - Visualization

---

## My ML Approach

### 1. Markov Chains (Statistical) 
- **What I've implemented**: N-gram based sequence generation
- **Order**: Configurable (bigrams, trigrams, etc.)
- **Why I like it**: Fast, interpretable, no training overhead
- **My use case**: Baseline for comparison with deep learning

### 2. Recurrent Neural Networks (Next Step)
- **Architecture I'm planning**: Character-level LSTM
- Embedding layer for character representation
- LSTM cells for learning long-term dependencies
- Softmax output for next-character prediction

### 3. Generative Adversarial Networks (Future Goal)
- **PassGAN-inspired** architecture
- Generator creates password candidates
- Discriminator distinguishes real vs. generated
- Adversarial training for realistic outputs

### My Training Strategy
- Pre-train on large breach datasets (32M+ passwords from RockYou)
- Fine-tune on domain-specific patterns
- Validate against held-out test sets
- Compare generation quality: Dictionary → Markov → RNN → GAN

### Expected Performance (Based on Research)
- **Markov chains**: 2-5x better than random dictionary
- **Neural networks**: 5-10x better than Markov
- **GANs (PassGAN)**: 10-20x better for complex passwords

---

## Research I'm Building On

**Key Papers I've studied:**
- PassGAN: A Deep Learning Approach for Password Guessing (Hitaj et al., 2017)
- Fast, Lean, and Accurate: Modeling Password Guessability Using Neural Networks (Melicher et al., 2016)
- The Tangled Web of Password Reuse (Das et al., 2014)
- NIST SP 800-63B: Digital Identity Guidelines

**Datasets I'm using:**
- RockYou (32M passwords from 2009 breach)
- SecLists password collections
- LinkedIn breach dataset
- Common password rankings (SplashData, NordPass)

**Tools I'm comparing against:**
- John the Ripper (Markov mode)
- Hashcat (rule-based + Markov)
- PCFG Cracker (probabilistic context-free grammars)

---

## What I'm Learning

**Technical Skills:**
- Cryptographic hash functions and security principles
- Statistical modeling with Markov chains
- Neural network architecture design
- Performance optimization in Python
- Large-scale data processing and analysis
- Comparative ML method evaluation

**Domain Knowledge:**
- Password attack vectors and methodologies
- ML applications in cybersecurity
- Ethical hacking principles
- Security research best practices
- Information theory (entropy, randomness)

**Development Practices:**
- Research-driven development
- Reproducible experiments
- Performance benchmarking
- Version control and documentation

---

## How I'm Evaluating Performance

To compare methods scientifically, I'm tracking:

**Success Rate:**
- % of passwords cracked in N guesses
- Time to first successful crack

**Efficiency:**
- Guesses per second
- Memory usage
- Training time (for ML models)

**Quality Metrics:**
- Character distribution similarity
- N-gram overlap with real passwords
- Perplexity scores

**My Comparative Analysis:**
- Dictionary baseline
- Markov chains (order 2, 3, 4)
- RNN models
- GAN models

---

## Installation & Usage
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/PasswordML.git
cd PasswordML

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run password analyzer
python analyzer.py

# Train and use Markov generator
python markov.py
```

---
