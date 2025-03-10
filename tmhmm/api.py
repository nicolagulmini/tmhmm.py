from collections import defaultdict

import numpy as np
import os.path

from tmhmm.model import parse
from tmhmm.hmm import viterbi, forward, backward

np.seterr(divide = 'ignore')


GROUP_NAMES = ('i', 'm', 'o')

DEFAULT_MODEL = os.path.join(os.path.dirname(__file__), 'TMHMM2.0.model')

def predict(sequence, model_or_filelike=DEFAULT_MODEL, compute_posterior=True):
    if isinstance(model_or_filelike, tuple):
        model = model_or_filelike
    else:
        header, model = parse(model_or_filelike)

    _, path = viterbi(sequence, *model)

    if compute_posterior:
        forward_table, constants = forward(sequence, *model)
        backward_table = backward(sequence, constants, *model)

        posterior = forward_table * backward_table
        _, _, _, char_map, label_map, name_map = model

        observations = len(sequence)
        states = len(name_map)

        table = np.zeros(shape=(observations, 3))
        for i in range(observations):
            group_probs = defaultdict(float)
            for j in range(states):
                group = label_map[j].lower()
                group_probs[group] += posterior[i, j]

            for k, group in enumerate(GROUP_NAMES):
                table[i, k] = group_probs[group]
        return path, table/table.sum(axis=1, keepdims=True)
    return path
