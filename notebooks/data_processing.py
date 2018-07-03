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


def grouped_train_val_test_split(df, train_size, val_size, test_size, feature_names, label_name):
    
    train = sample[:n_train]
    validation = sample[n_train:n_train+n_valid]
    test = sample[n_train+n_valid:]
    
    train_idx = family_data['Target'].isin(train)
    validation_idx = family_data['Target'].isin(validation)
    test_idx = family_data['Target'].isin(test)

    X_train = family_data[train_idx][feature_names].values
    X_validation = family_data[validation_idx][feature_names].values
    X_test = family_data[test_idx][feature_names].values

    y_train = family_data[train_idx]['Label'].replace({'Random': 0, 'Fam': 1}).values
    y_validation = family_data[validation_idx]['Label'].replace({'Random': 0, 'Fam': 1}).values
    y_test = family_data[test_idx]['Label'].replace({'Random': 0, 'Fam': 1}).values
