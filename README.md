<p align="center">
  April 2018 DoM Interview Assessment
</p>

<p align="center">
  <a href="http://travis-ci.org/mycaule/dom-assessment"><img src="https://api.travis-ci.org/mycaule/dom-assessment.svg?branch=master" alt="Build Status"></a>
  <br>
  <br>
</p>

### Usage

Small program to plays checkers in the terminal against an AI.

```
$ source .venv/bin/activate
$ pip freeze > requirements.txt
$ make test
$ make
```

### Allowed moves

```
  __0_1_2_3_4_5_6_7__
0 |   b   b   b   b |
1 | b   b   b   b   |
2 |   b   b   b   b |
3 | _   _   _   _   |
4 |   _   _   _   _ |
5 | w   w   w   w   |
6 |   w   w   w   w |
7 | w   w   w   w   |
  -------------------
```
If you consider *(i,j)* coordinates as in Excel spreadsheets:
 - *i* values in rows,
 - *j* values in columns.

the possible values *Def(b)* and allowed moves *All(b)* for black pieces are:

```
Def(b) = { (i, j) in [0;7] x [0;7]
            with i and j having opposite parities}
All(b) = { [(i, j), (i+1, j±1)] / (i, j) in Def(b)}
```

The *sigma* function reverses the black and white position in a symmetric manner :

```
sigma: (i, j) => (7-i, 7-j)
sigma o sigma = Id
All(w) = sigma(All(b))
```

Kings can move through the whole board in both directions meaning that:
```
All(B) = All(W) = All(w) U All(b)
```

Considering these properties, it suffices to study the black allowed moves.
We compute the list of non-capturing moves and capturing moves separately.

### Playing strategy

- Capture if possible, maximize number of pieces captured,
- If no capture is possible, choose the next move that minimizes or maximize inertia towards an adaptive attitude if we are outnumbered or not.

To go further, we can study more efficient openings and implement strategies from the litterature:

* 1950 - Claude Shannon
* 1952 - Perceptron
* 1958 - MiniMax with Alpha Beta pruning
* 1982 - Reinforcement learning
* 1990 - Chinook
* 1990 - Deep Blue
* 2010 - Alpha Go

### Going further

[Sam Ragusa - Checkers with Reinforcement learning](https://github.com/SamRagusa/Checkers-Reinforcement-Learning)
