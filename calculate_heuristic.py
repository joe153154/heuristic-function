import random
import pandas as pd
from math import sqrt
from itertools import combinations

# 計算兩點之間的歐幾里德距離
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# 計算所有座標之間的距離和啟發式函數值
def get_distances_and_heuristic_values(coords, demands):
    distances = []
    heuristic_values = []
    coord_pairs = list(combinations(coords, 2))  # 生成所有座標對

    if not coord_pairs:
        return [], [], []  # 如果 coord_pairs 為空,返回空列表

    for (x1, y1), (x2, y2) in coord_pairs:
        distance = calculate_distance(x1, y1, x2, y2)
        distances.append(distance)
        demand1 = demands[coords.index((x1, y1))]
        demand2 = demands[coords.index((x2, y2))]
        heuristic_value = 0.7 * distance + 0.3 * (demand1 + demand2)
        heuristic_values.append(heuristic_value)

    return list(zip(*coord_pairs)), distances, heuristic_values

def main():
    # 生成隨機座標及需求值
    coords = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(100)]
    demands = [random.randint(0, 100) for _ in range(100)]

    # 計算距離及啟發式函數值
    coord_pairs, distances, heuristic_values = get_distances_and_heuristic_values(coords, demands)

    # 將計算結果存入 DataFrame
    df = pd.DataFrame({
        'X1': [x1 for (x1, y1) in coord_pairs[0]] if coord_pairs else [],
        'Y1': [y1 for (x1, y1) in coord_pairs[0]] if coord_pairs else [],
        'X2': [x2 for (x2, y2) in coord_pairs[1]] if coord_pairs else [],
        'Y2': [y2 for (x2, y2) in coord_pairs[1]] if coord_pairs else [],
        'demand1': [demands[coords.index((x1, y1))] for (x1, y1) in coord_pairs[0]] if coord_pairs else [],
        'demand2': [demands[coords.index((x2, y2))] for (x2, y2) in coord_pairs[1]] if coord_pairs else [],
        'distances': distances,
        'heuristic': heuristic_values
    })

    print(df)
    df.to_csv("heuristic_df.csv")

if __name__ == "__main__":
    main()