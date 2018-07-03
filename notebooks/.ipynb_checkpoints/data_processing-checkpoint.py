import numpy as np
import pandas as pd

def undersample(df, column_name, seed=42):
    
    result = df.copy()
    data_counts = df[column_name].value_counts()
    labels = data_counts.drop(data_counts.idxmin(), inplace=False).index.values

    for label in labels:
        n_to_drop = data_counts.loc[label] - min(data_counts)
        idx = df[df[column_name] == label].index.values
        to_drop = np.random.choice(idx, size=n_to_drop, replace=False)
        result.drop(to_drop, axis='index', inplace=True)
        
    return result
