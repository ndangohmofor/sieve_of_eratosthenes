# The Sieve of Eratosthenes

The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to any given limit. It's an efficient way to find primes and is often used in computer science and mathematics. Here's how the algorithm works:

# Algorithm Steps:

### 1. Create a List of Numbers:

* Start with a list of numbers from 2 up to the desired maximum (n).

### 2. Initial Sieving Process:

* Begin with the first number in the list (which will be 2, the smallest prime number).
* Mark all multiples of this number (except the number itself) as non-prime.

### 3. Repeat for Next Unmarked Number:

* Move to the next number in the list that hasn't been marked as non-prime.
* Again, mark all multiples of this number (except the number itself) as non-prime.
* Continue this process until you've processed each number in the list up to the square root of n. Numbers beyond this point don't need to be checked because their multiples would have already been marked as non-prime by smaller numbers.

### 4. Remaining Unmarked Numbers:

* The numbers that remain unmarked at the end of this process are the prime numbers.

# Example:

Let's say we want to find all prime numbers up to 10. Here's how we would apply the Sieve of Eratosthenes:

**1. List of Numbers: 2, 3, 4, 5, 6, 7, 8, 9, 10**

**2. Initial Number is 2:**

* Mark multiples of 2: 4, 6, 8, 10

**3. Next Unmarked Number is 3:**

* Mark multiples of 3: 6 (already marked), 9

**4. Next Unmarked Number is 5:**

* Since 5^2 > 10, we stop the process.

**5. Remaining Unmarked Numbers:**

* 2, 3, 5, 7

So, the prime numbers up to 10 are 2, 3, 5, and 7.