# Computational Mathematics Projects

Collection of computational experiments exploring numerical methods, probabilistic techniques, and mathematical structure through simulation and visualization.

## Projects

### 1. Prime Distribution

**What it Does:**  
Analyzes how prime numbers are distributed by counting primes in fixed intervals and comparing observed behavior with theoretical expectations.

**Core Idea:**  
Empirical exploration of the Prime Number Theorem through interval-based analysis.

**Approach:**  
	•	Partition integers into intervals of size 100 up to 10⁶  
	•	Count primes within each interval  
	•	Compute expected density using 100/ln(n)  
	•	Measure local deviation from the theoretical estimate  

**How it Works:**  
Prime counts are computed across uniform intervals, producing a distribution of observed densities. These are compared against the asymptotic estimate given by the Prime Number Theorem. The deviation between observed and expected values highlights fluctuations in prime density at finite scales.

**Features:**  
	•	Interval-based prime counting  
	•	Frequency distribution visualization  
	•	Local deviation analysis from theoretical expectation  

**Stack:** Wolfram Mathematica

<p align="center">
<img src="Assets/Prime-Distribution-Plots.jpeg" width="800"></p>

### 2. Monte Carlo π Estimation

**What it Does:**  
Approximates the value of π using random sampling and visualizes convergence over time.

**Core Idea:**  
Geometric probability via Monte Carlo simulation.

**Approach:**  
	•	Uniformly sample points in a square  
	•	Classify points using the condition x² + y² ≤ 1  
	•	Estimate π from the ratio of points inside the quarter circle  

**How it Works:**  
Random points are generated within a bounded square. Points that fall inside the unit quarter circle are counted, and the ratio of inside to total points is used to approximate π. As the number of samples increases, the estimate converges toward the true value.

**Features:**  
	•	Stochastic sampling-based approximation  
	•	Real-time convergence visualization  
	•	Geometric interpretation of probability  

**Stack:** Python, Matplotlib

<p align="center">
<img src="Assets/Monte-Carlo-Pi.png" width="500"></p>

## 3. Pseudo-Polyomino Enumeration

**What it does:**  
Generates and counts unique pseudo-polyomino shapes of size N by iteratively constructing connected block configurations and eliminating duplicates under rotational symmetry.

**Core Idea:**  
Combinatorial growth of connected structures with canonicalization to remove symmetry-equivalent duplicates.

**How it Works:**  
The algorithm begins with a single unit block and incrementally builds larger shapes by attaching new blocks to existing ones. At each step, all possible adjacent positions (including diagonal directions) are considered for expansion, ensuring connectivity.

To avoid counting equivalent shapes multiple times, each generated configuration is transformed under rotational symmetries (0°, 90°, 180°, 270°). Each transformed version is normalized by translating it to a common origin and sorting coordinates. The lexicographically smallest representation is selected as the canonical form.

Only canonical representations are retained, ensuring that symmetric duplicates are removed. This process is repeated iteratively until shapes of size N are constructed, at which point the total count is reported.

**Features:**
- Iterative generation of connected block structures  
- Support for 8-directional adjacency (including diagonals)  
- Symmetry reduction using rotational canonicalization  

**Stack:**  
Python
