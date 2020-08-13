import numpy as np
import pandas as pd


def solve(adj):
    visited = {}
    
    start = adj.iloc[0]
    for index, row in adj.iterrows():
        print("INDEX: ", index)
        print("ROW: ", row)


def main():
    adj = pd.read_csv('adjacency.csv', index_col='compared')
    solve(adj)


if __name__ == "__main__":
    main()