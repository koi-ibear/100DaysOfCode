
"""
🌸 Medium 1007. Minimum Domino Rotations For Equal Row
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""
def minDominoRotations(self, A, B):
    for x in [A[0],B[0]]:
        if all(x in d for d in zip(A, B)):
            return len(A) - max(A.count(x), B.count(x))
    return -1