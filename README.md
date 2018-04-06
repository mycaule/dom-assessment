<p align="center">
  April 2018 DoM Interview Assessment
</p>

<p align="center">
  <a href="http://travis-ci.org/mycaule/dom-assessment"><img src="https://api.travis-ci.org/mycaule/dom-assessment.svg?branch=master" alt="Build Status"></a>
  <br>
  <br>
</p>

### Usage

```
$ source .venv/bin/activate
$ pip freeze > requirements.txt
$ make test
$ make
```

### Allowed Moves

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
If you consider (i,j) coordinates as in Excel spreadsheets:
 - i values in rows,
 - j values in columns.

the possible values for black pieces are:
Def_b = { (i, j) in [0;7] x [0;7]
            with i and j having opposite parities}

The sigma function reverses the black and white position in a symmetric manner
such that the f function maps (i, j) to :
 sigma: (i, j) => (7-i, 7-j)

```
sigma o sigma = Id
Def_w = sigma(Def_b)
```

Kings can move through the whole board in both directions meaning that:
```
Def_B = Def_W = Def_w U Def_b
```

Considering these properties, it suffices to study the black allowed moves.

For a piece x, computing All(x) involves starting from Def(x) then eliminating squares occupied by its neighbors, then computing recursively possible moves from the tail if capture is done.

### Play

Strategy:
- Capture if possible, maximize number of pieces captured
- If no capture is possible, choose the next move that minimize inertia (defensive attitude) or that maximize inertia (offensive attitude)

TODO Write small history of resolution algorithms since Perceptron in 1950.
Modern technique is reinforcement learning as popularized by Alpha Go.
