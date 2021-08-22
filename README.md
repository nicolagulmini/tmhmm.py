# Introduction

This repository houses a Python 3.5+ implementation of transmembrane helix
hidden Markov model ([TMHMM](http://www.cbs.dtu.dk/services/TMHMM/)) originally
described in:

E\. L.L. Sonnhammer, G. von Heijne, and A. Krogh. **A hidden Markov model for
predicting transmembrane helices in protein sequences**. In J. Glasgow,
T. Littlejohn, F. Major, R. Lathrop, D. Sankoff, and C. Sensen, editors,
Proceedings of the Sixth International Conference on Intelligent Systems for
Molecular Biology, pages 175-182, Menlo Park, CA, 1998. AAAI Press.

To read the original readme with the instructions for the usage of this software, check [this link](https://github.com/dansondergaard/tmhmm.py).

## How to use

`!python -m pip install git+https://github.com/nicolagulmini/tmhmm.py` and then `import tmhmm`.
To predict a protein do
```
annotation, posterior = tmhmm.predict(sequence)
```
where `posterior` is a vector of `len(sequence)` 3-dim vectors (one for each amino acid) with:
1. probability of being inside
2. probability of being transmembrane
3. probability of being outside.
