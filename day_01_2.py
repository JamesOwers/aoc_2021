import sys

import pandas as pd

if __name__ == "__main__":
    path = sys.argv[1]
    ser = pd.read_csv(path, header=None).squeeze()
    ser = ser.rolling(3).sum()
    print((ser > ser.shift(1)).sum()) 
