# common
import numpy as np
import pandas as pd
from pandas import DataFrame

# URL
url_winequality_data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"


# working place. everything
def homework(url_winequality_data, n):
    data = pd.read_csv(url_winequality_data, sep=";")
    data["volatile_acidity_group"] = pd.qcut(data["volatile acidity"], n)
    quality_five_data = data[data["quality"] == 5]
    group_means = quality_five_data.groupby("volatile_acidity_group")["alcohol"].mean()
    return group_means.min()


print(homework(url_winequality_data, 5))
