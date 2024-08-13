# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:52:50 2024

@author: Nelson Guio
"""

def robot_collisions(sequence: str) -> str:
    n = len(sequence)
    collisions = [0] * n
    seq_list = list(sequence)

    # Revisar colisiones iniciales
    for i in range(n - 1):
        if seq_list[i] == 'R' and seq_list[i + 1] == 'L':
            collisions[i] += 1
            collisions[i + 1] += 1
            seq_list[i] = 'L'
            seq_list[i + 1] = 'R'

    # Revisar posibles colisiones subsiguientes
    for i in range(n - 1):
        if seq_list[i] == 'R' and seq_list[i + 1] == 'L':
            collisions[i] += 1
            collisions[i + 1] += 1

    return ' '.join(map(str, collisions))
