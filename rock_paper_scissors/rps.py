#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']

  if n == 0:
    return [[]]

  if n == 1:
    return [[x] for x in options]

  if n == 2:
    return [[x, j] for x in options for j in options]

  if n == 3:
    return [[x, j, d] for x in options for j in options for d in options]

  if n == 4:
    return [[x, j, d, a] for x in options for j in options for d in options for a in options]
  
  if n == 5:
    return [[x, j, d, a, w] for x in options for j in options for d in options for a in options for w in options]


print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')