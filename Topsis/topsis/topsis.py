import sys
import pandas as pd
import numpy as np


def read_file(input_file):
    if input_file.endswith('.csv'):
        return pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        return pd.read_excel(input_file)
    else:
        print("Error: Only CSV or XLSX files supported")
        sys.exit()


def topsis(input_file, weights, impacts, output_file):
    data = read_file(input_file)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit()

    try:
        decision = data.iloc[:, 1:].astype(float)
    except Exception:
        print("Error: Non numeric values found in criteria columns")
        sys.exit()

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != decision.shape[1] or len(impacts) != decision.shape[1]:
        print("Error: Number of weights, impacts and criteria must be same")
        sys.exit()

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be either + or -")
            sys.exit()

    weights = np.array(weights, dtype=float)

    norm = decision / np.sqrt((decision ** 2).sum())
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data['Topsis Score'] = score
    data['Rank'] = data['Topsis Score'].rank(method='max', ascending=False)

    data.to_csv(output_file, index=False)
    print("Result successfully written to", output_file)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <InputDataFile> <Weights> <Impacts> <OutputFile>")
        sys.exit()

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)
