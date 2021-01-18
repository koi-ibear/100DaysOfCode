## Data Structure & Algorithm Practices

### 1. Backtracking
	[Backtracking](https://www.geeksforgeeks.org/backtracking-introduction/) is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time 
	The Algorithm begins to build up a solution, starting with an empty solution set S. S = {}

	Add to S the first move that is still left (All possible moves are added to S one by one). This now creates a new sub-tree s in the search tree of the algorithm.
	Check if S+s satisfies each of the constraints in C.
	If Yes, then the sub-tree s is “eligible” to add more “children”.
	Else, the entire sub-tree s is useless, so recurs back to step 1 using argument S.
	In the event of “eligibility” of the newly formed sub-tree s, recurs back to step 1, using argument S+s.
	If the check for S+s returns that it is a solution for the entire data D. Output and terminate the program.
	If not, then return that no solution is possible with the current s and hence discard it.

```

void findSolutions(n, other params) :
    if (found a solution) :
        solutionsFound = solutionsFound + 1;
        displaySolution();
        if (solutionsFound >= solutionTarget) : 
            System.exit(0);
        return

    for (val = first to last) :
        if (isValid(val, n)) :
            applyValue(val, n);
            findSolutions(n+1, other params);
            removeValue(val, n);
```