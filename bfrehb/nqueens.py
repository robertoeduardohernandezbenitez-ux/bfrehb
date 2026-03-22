def n_queens_tree(n,x=None):
    """Generates all the solutions to the n-queens problem as lists of column indices."""
    if x is None:
        x=[]
    if len(x)==n:
        yield x[:]
    else:
        choices= [i for i in range(n) if i not in x and all(abs(i-x[j])!=len(x)-j for j in range(len(x)))]
        for choice in choices:
            x.append(choice)
            yield from n_queens_tree(n, x)
            x.pop()