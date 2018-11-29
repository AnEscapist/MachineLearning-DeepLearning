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

In general terms, the expected information gain is the change in information entropy **H** from a prior state to a state that takes some information as given.

<a href="https://www.codecogs.com/eqnedit.php?latex=g(D,&space;A)&space;=&space;H(D)&space;-&space;H(D|A)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g(D,&space;A)&space;=&space;H(D)&space;-&space;H(D|A)" title="g(D, A) = H(D) - H(D|A)" /></a>
  
where **H(D|A)** is the conditional entropy of **D** given the value of attribute A.

Information entropy:

<a href="https://www.codecogs.com/eqnedit.php?latex=H(D)&space;=&space;-\sum_{k=1}^{K}\frac{|C_k|}{|D|}log_2\frac{|C_k|}{|D|}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(D)&space;=&space;-\sum_{k=1}^{K}\frac{|C_k|}{|D|}log_2\frac{|C_k|}{|D|}" title="H(D) = -\sum_{k=1}^{K}\frac{|C_k|}{|D|}log_2\frac{|C_k|}{|D|}" /></a>

Conditional entropy:

<a href="https://www.codecogs.com/eqnedit.php?latex=H(D|A)&space;=&space;\sum_{i=1}^{n}\frac{|D_i|}{|D|}H(D_i)=-\sum_{i=1}^{n}\frac{|D_i|}{|D|}\sum_{k=1}^{k}\frac{|D_{ik}|}{|D_i|}log_2\frac{|D_{ik}|}{|D_i|}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H(D|A)&space;=&space;\sum_{i=1}^{n}\frac{|D_i|}{|D|}H(D_i)=-\sum_{i=1}^{n}\frac{|D_i|}{|D|}\sum_{k=1}^{k}\frac{|D_{ik}|}{|D_i|}log_2\frac{|D_{ik}|}{|D_i|}" title="H(D|A) = \sum_{i=1}^{n}\frac{|D_i|}{|D|}H(D_i)=-\sum_{i=1}^{n}\frac{|D_i|}{|D|}\sum_{k=1}^{k}\frac{|D_{ik}|}{|D_i|}log_2\frac{|D_{ik}|}{|D_i|}" /></a>

where C<sub>k is the number of samples of class k.

## Example:

| QQ  | Gender |  active_infor  | is_lost|
| --- | --- | --- | --- |
| 1  | M  | High | 0 |
| 2  | F  | Mid | 0 |
| 3  | M  | Low | 1 |
| 4  | F  | High | 0 |
| 5  | M  | High | 0 |
| 6  | M  | Mid | 0 |
| 7  | M  | Mid | 1 |
| 8  | F  | Mid | 0 |
| 9  | F  | Low | 1 |
| 10  | F  | Mid | 0 |
| 11  | F  | High | 0 |
| 12  | M  | Low | 1 |
| 13  | F  | Low | 1 |
| 14  | M  | High | 0 |
| 15  | M  | High | 0 |

Statistical Chart:

|    | Lost |  Non-lost  | Total|
| --- | --- | --- | --- |
| Overall  | 5  | 10 | 15 |
| Male  | 3  | 5 | 8 |
| Female  |2  | 5 | 7 |
| High  | 0  | 6 | 6 |
| Mid  | 1  | 4 | 5 |
| Low  | 4  | 0 | 4 |

From the chart, we get three entropies:

1st:

























