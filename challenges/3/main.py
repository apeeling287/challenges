import pandas as pd
from datetime import datetime
data = [
  {
    "id": 0,
    "type": "pm_10",
    "time_series": [
      {
        "timestamp": 1653322292,
        "value": 10
      },
      {
        "timestamp": 1653323192,
        "value": 11.226996442121207
      },
      {
        "timestamp": 1653324092,
        "value": 16.84813802420236
      },
      {
        "timestamp": 1653324992,
        "value": 14.809332727104243
      },
      {
        "timestamp": 1653325892,
        "value": 9.982512708032488
      },
      {
        "timestamp": 1653326792,
        "value": 8.90423556603678
      },
      {
        "timestamp": 1653327692,
        "value": 9.858466753859364
      },
      {
        "timestamp": 1653328592,
        "value": 6.487251523096642
      },
      {
        "timestamp": 1653329492,
        "value": 4.117500029731538
      },
      {
        "timestamp": 1653330392,
        "value": 7.864398337428433
      },
      {
        "timestamp": 1653331292,
        "value": 8.920773505271907
      },
      {
        "timestamp": 1653332192,
        "value": 8.83970726114226
      },
      {
        "timestamp": 1653333092,
        "value": 9.691313315146461
      },
      {
        "timestamp": 1653333992,
        "value": 9.099854566160698
      },
      {
        "timestamp": 1653334892,
        "value": 8.920473326322174
      },
      {
        "timestamp": 1653335792,
        "value": 8.427198168996586
      },
      {
        "timestamp": 1653336692,
        "value": 10
      },
      {
        "timestamp": 1653337592,
        "value": 10.178507162482122
      },
      {
        "timestamp": 1653338492,
        "value": 11.842922951280933
      },
      {
        "timestamp": 1653339392,
        "value": 9.238576319012324
      },
      {
        "timestamp": 1653340292,
        "value": 10.474561249566893
      },
      {
        "timestamp": 1653341192,
        "value": 10.502754383669908
      },
      {
        "timestamp": 1653342092,
        "value": 8.494046880951373
      },
      {
        "timestamp": 1653342992,
        "value": 13.781430399167352
      },
      {
        "timestamp": 1653343892,
        "value": 16.776179173243328
      },
      {
        "timestamp": 1653344792,
        "value": 15.032937132824316
      },
      {
        "timestamp": 1653345692,
        "value": 9.322448553824149
      },
      {
        "timestamp": 1653346592,
        "value": 10.664421710532096
      },
      {
        "timestamp": 1653347492,
        "value": 9.383865702037092
      },
      {
        "timestamp": 1653348392,
        "value": 7.880174984118742
      },
      {
        "timestamp": 1653349292,
        "value": 3.8994303830309684
      },
      {
        "timestamp": 1653350192,
        "value": 7.2542887797147255
      }
    ]
  },
  {
    "id": 1,
    "type": "pm_10",
    "time_series": [
      {
        "timestamp": 1653322292,
        "value": 10
      },
      {
        "timestamp": 1653323192,
        "value": 8.78688100721783
      },
      {
        "timestamp": 1653324092,
        "value": 8.514432264700254
      },
      {
        "timestamp": 1653324992,
        "value": 9.522760838450523
      },
      {
        "timestamp": 1653325892,
        "value": 8.531370176901811
      },
      {
        "timestamp": 1653326792,
        "value": 10.4753014733677
      },
      {
        "timestamp": 1653327692,
        "value": 11.85391799340847
      },
      {
        "timestamp": 1653328592,
        "value": 12.35352760316995
      },
      {
        "timestamp": 1653329492,
        "value": 14.307109544771492
      },
      {
        "timestamp": 1653330392,
        "value": 13.01242291205643
      },
      {
        "timestamp": 1653331292,
        "value": 11.491498395062019
      },
      {
        "timestamp": 1653332192,
        "value": 9.20713624326272
      },
      {
        "timestamp": 1653333092,
        "value": 11.061583091695645
      },
      {
        "timestamp": 1653333992,
        "value": 7.228247465776794
      },
      {
        "timestamp": 1653334892,
        "value": 6.1465433530765
      },
      {
        "timestamp": 1653335792,
        "value": 3.7465119723248197
      },
      {
        "timestamp": 1653336692,
        "value": 10
      },
      {
        "timestamp": 1653337592,
        "value": 14.80413906843554
      },
      {
        "timestamp": 1653338492,
        "value": 10.868392567416429
      },
      {
        "timestamp": 1653339392,
        "value": 13.689256010075539
      },
      {
        "timestamp": 1653340292,
        "value": 13.151727511134983
      },
      {
        "timestamp": 1653341192,
        "value": 12.020774244020608
      },
      {
        "timestamp": 1653342092,
        "value": 7.132458976273806
      },
      {
        "timestamp": 1653342992,
        "value": 7.908768158207678
      },
      {
        "timestamp": 1653343892,
        "value": 9.473761884280545
      },
      {
        "timestamp": 1653344792,
        "value": 10.171763426554737
      },
      {
        "timestamp": 1653345692,
        "value": 13.0652605110399
      },
      {
        "timestamp": 1653346592,
        "value": 8.158532591910593
      },
      {
        "timestamp": 1653347492,
        "value": 7.570641235862247
      },
      {
        "timestamp": 1653348392,
        "value": 10.503420750639428
      },
      {
        "timestamp": 1653349292,
        "value": 10.996507121525559
      },
      {
        "timestamp": 1653350192,
        "value": 9.360871740393716
      }
    ]
  }
]

## Normalise the data
df = pd.DataFrame(data)
df_cleaned = pd.json_normalize(data, record_path="time_series", 
                               meta=["id","type"])
print(df_cleaned)
df_cleaned.head()
#df_cleaned.set_index(["id","type"], inplace=True)
#df_cleaned.to_csv(r"C:\Users\annabel.peel\Documents\A29\Annabel Peel\Personal\Interview\flattened_data.csv")
df_cleaned["datetime"] = pd.to_datetime(df_cleaned["timestamp"], unit="s")
df_cleaned.head()
df_cleaned.set_index("datetime", inplace=True)
df_cleaned.sort_index(inplace=True)
df_cleaned.head()
df_cleaned['rolling_mean'] = df_cleaned["value"].rolling("1H").mean()
df_cleaned.head()
max_rolling_mean = df_cleaned["rolling_mean"].max()
max_rolling_mean_time = df_cleaned["rolling_mean"].idxmax()

print(f"Maximum rolling mean value: {max_rolling_mean}")
print(f"At time: {max_rolling_mean_time}")