# Decision Tree

## Introduction
The idea of decision tree is simple: if-else statement.

By using if-else statement, decision tree can segment the data.

# Information Entropy

**Equation of information entropy:**

<a href="https://www.codecogs.com/eqnedit.php?latex=H(X)&space;=&space;\sum_{i=1}^{n}p(x_i)I(x_i)&space;=&space;-\sum_{i=1}^{n}P(x_i)log_2P(x_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(X)&space;=&space;\sum_{i=1}^{n}p(x_i)I(x_i)&space;=&space;-\sum_{i=1}^{n}P(x_i)log_2P(x_i)" title="H(X) = \sum_{i=1}^{n}p(x_i)I(x_i) = -\sum_{i=1}^{n}P(x_i)log_2P(x_i)" /></a>

where **I(x)** represents the information of random variables, and **p(x)** denotes the probability of event x

**Explanation:**

```
Game A: High-active usesrs is 20%, mid-active users is 30%, low-active users is 50%
Game B: High-active usesrs is 5%, mid-active users is 5%, low-active users is 90%
```

<a href="https://www.codecogs.com/eqnedit.php?latex=H(A)&space;=&space;-(0.2&space;*&space;log_20.2&space;&plus;&space;0.3&space;*&space;log_20.3&space;&plus;&space;0.5&space;*&space;log_20.5)&space;=&space;1.485" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(A)&space;=&space;-(0.2&space;*&space;log_20.2&space;&plus;&space;0.3&space;*&space;log_20.3&space;&plus;&space;0.5&space;*&space;log_20.5)&space;=&space;1.485" title="H(A) = -(0.2 * log_20.2 + 0.3 * log_20.3 + 0.5 * log_20.5) = 1.485" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=H(B)&space;=&space;-(0.05&space;*&space;log_20.05&space;&plus;&space;0.05&space;*&space;log_20.05&space;&plus;&space;0.9&space;*&space;log_20.9)&space;=&space;0.569" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(B)&space;=&space;-(0.05&space;*&space;log_20.05&space;&plus;&space;0.05&space;*&space;log_20.05&space;&plus;&space;0.9&space;*&space;log_20.9)&space;=&space;0.569" title="H(B) = -(0.05 * log_20.05 + 0.05 * log_20.05 + 0.9 * log_20.9) = 0.569" /></a>

```
The entropy of Game A is greater than that of Game B, so the nondeterminacy of A is higher than B. 
Simply sppeaking, Game B is in a stage of either rising or descent, it is highly predictable of its future, 
so it has a lower entropy.
However, Game A has a more nondeterminacy than Game B, therefore A has a higher entropy.
```

# Information Gain

## Definition

In general terms, the expected information gain is the change in information entropy H from a prior state to a state that takes some information as given.
