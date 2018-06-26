# Theory of Computation
***

### Definition
***
Study of mathematical machine or system, often called automata (deals with computational problem).

### Theory of Formal Languages
***
In mathematics and computer science a formal language is set of **strings** of **symbol** together with a set of rules (**grammar**).

So we need to:
**Grammar** ---(to generate)---> **Language** ---(accepted by)---> **Machine(Automata)**

### Terminology
***
* **Symbol**: Basic building blocks which can be any character as token.

	example: In english alphabet we 26 small (a to z) and 26 capital (A to Z) symbols (letters).

	* English have 26 symbols. More symbols can generate more words, so we can express ourself in a better way.

	* We could have language for say fan with just 2 symbols. One for **ON** and one for **OFF**. It all depends on the complexity of the problem.

	* In formal automata we could have only two symbols like **a** and **b** or say  **0** or **1**.

* **Alphabet**: **Finite non-empty set** of symbols (set of letters).

	example: In english we have {a, b, c, ..., z}

	In formal language we denotes alphabet with **Σ**. So we can have Alphabet with teo symbol, **Σ = {0, 1}** or **Σ = {a, b}**

* **String**: Finite sequence of symbols.

	example: In english **car** is a string. It is already pre-difined and compiled in a dictionary (Oxford Dictionary for example).

* **Language**: Set of a string.

	In Formal language we can have **Language L = {001, 110}** build by **strings 001** and **110** which is built by **alphabet Σ = {0, 1}** which is built from two **symbols 0** and **1**.

### Basic operations on strings
***
Strings are basically denoted by Capital Letter (English), usaually W.

* Length of String: It is denoted by **|W|**.

* Null is a string of length 0 and is denoted by **ϵ**. So |ϵ| = 0.

* Concatenation of strings. 
	Say we have 2 strings **W1 = 'abc'** and **W2 = 'ac'**.
	So concatenation of strings **W1** and **W2** is denoted by **W1.W2 = abcac**.
	* |W1| + |W2| = |W1.W2|
	* W1.W2 ≠ W2.W1 but W.ϵ = ϵ.W = W

* Reverse of a string: It is denoted by **W<sup>R</sup>**.
	* |W| = |W<sup>R</sup>|

* Prefix and Sufix: Set of substring of W from starting and ending position respectively.
	Say W = abaa
	Now prefix of W denoted by **P(W)** = {ϵ, a, ab, aba, abaa}
	Sufix of W denoted by **S(W)** = {ϵ, a, aa, baa, abaa}

* Substring: As it sounds. It's a substring. Sequence is maintain
	Say W = abbbaca

	abb -> is a substring
	bab -> is not a substring
	cab -> is not a substring
	bbb -> is a substring

	Say we have a string where all the symbols are unique: **GATE**

	So how many substring we can have?

	| Substring(↓)/Size(→) | 0 | 1 | 2 | 3 | 4 |
	|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
	| → | ϵ | G | GA | GAT | GATE |
	| → | - | A | AT | ATE | - |
	| → | - | T | TE | - | - |
	| → | - | E | - | - | - |

	That's equals to 11.

	This can be calculated by **n\*(n+1)/2 + 1**, where |W| = n

### Kleene Closure
***
Denoted by Σ<sup>\*</sup>. The set Σ<sup>\*</sup> is the infinite set of all possible strings of all possible lengths over Σ including ϵ.

Let Σ = {a, b}

Now,
Σ<sup>0</sup> = {ϵ}
Σ<sup>1</sup> = {a, b}
Σ<sup>2</sup> = {aa, ab, ba, bb}
:
:
Σ<sup>k</sup> = {W | |W| = k}
:
:
Σ<sup>∞</sup> = {W | |W| = ∞}

Union of all these sets is Σ<sup>\*</sup>.

<a href="https://www.codecogs.com/eqnedit.php?latex={\sum}^*&space;=&space;\bigcup_{k=0}^{\infty}\left&space;\{&space;W&space;|&space;|W|&space;=&space;k&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\sum}^*&space;=&space;\bigcup_{k=0}^{\infty}\left&space;\{&space;W&space;|&space;|W|&space;=&space;k&space;\right&space;\}" title="{\sum}^* = \bigcup_{k=0}^{\infty}\left \{ W | |W| = k \right \}" /></a>

Also we have,

<a href="https://www.codecogs.com/eqnedit.php?latex={\sum}^&plus;&space;=&space;\bigcup_{k=1}^{\infty}\left&space;\{&space;W&space;|&space;|W|&space;=&space;k&space;\right&space;\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\sum}^&plus;&space;=&space;\bigcup_{k=1}^{\infty}\left&space;\{&space;W&space;|&space;|W|&space;=&space;k&space;\right&space;\}" title="{\sum}^+ = \bigcup_{k=1}^{\infty}\left \{ W | |W| = k \right \}" /></a>

### Grammar, Language, Automata
***
![](img/1.1.png)

