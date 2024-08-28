import pandas as pd
df = pd.read_json(r"C:\Users\annabel.peel\Downloads\sensors.json")
df.set_index("id","time_series")
print(df)
