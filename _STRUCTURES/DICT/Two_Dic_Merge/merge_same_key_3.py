import numpy as np

d1 = {(1, "Autumn"): np.array([2.5, 4.5, 7.5, 9.5]), (1, "Spring"): np.array([10.5, 11.7, 12.3, 15.0])}
d2 = {(1, "Autumn"): np.array([10.2, 13.3, 15.7, 18.8]), (1, "Spring"): np.array([15.6, 20, 23, 27])}
d3 = {k: np.concatenate((d1.get(k, np.array([])), d2.get(k, np.array([]))))
      for k in set(d1.keys()).union(set(d2.keys()))}

print(d3)

# {(1, 'Autumn'): array([ 2.5,  4.5,  7.5,  9.5, 10.2, 13.3, 15.7, 18.8]),
# (1, 'Spring'): array([10.5, 11.7, 12.3, 15. , 15.6, 20. , 23. , 27. ])}