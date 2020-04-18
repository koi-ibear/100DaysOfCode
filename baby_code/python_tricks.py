### flatten nested list
"""
e.g. a = [[1,2,5],[4,3]]

hint: multiple for loops, move inward from out-most layer
"""
[j for i in a for j in i]

### unpivot
"""
melt(id_var, value_var, value_name)
"""
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                    'B': {0: 1, 1: 3, 2: 5},
                    'C': {0: 2, 1: 4, 2: 6}})


df.melt(id_vars='A', value_vars=['B','C'], var_name='new')

df = pd.DataFrame(
    {"Item": ['Item0', 'Item0', 'Item0', 'Item1'],
    'CType':['Gold', 'Bronze', 'Gold', 'Silver'],
    'USD': [1, 2, 3, 4],
    'EU':   [1.1, 2.2, 3.3, 4.4]
})