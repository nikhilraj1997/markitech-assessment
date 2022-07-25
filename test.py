import pandas as pd

capacity_raw_data = {"01A": [19, 11, 4, 4], "01B": [24, 13, 5, 6], "01C": [
    23, 16, 3, 4], "02A": [19, 12, 3, 4], "01E": [15, 10, 2, 3]}

df_capacity = pd.DataFrame(
    capacity_raw_data, index=["Total", "Full Time", "Part Time", "Casual"], columns=["01A", "01B", "01C", "01E", "02A"])


for i in range(min(len(df_capacity), 5)):
    for col in df_capacity.columns:
        print(df_capacity)
