import json, pandas as pd
 
df = pd.read_csv("finops/focus_cloudshop_2026Q3.csv", parse_dates=["ChargePeriodStart"])
df["ChargePeriodStart"] = df["ChargePeriodStart"].dt.tz_localize(None)
df["Month"] = df["ChargePeriodStart"].dt.to_period("M")
df["Tags"] = df["Tags"].apply(json.loads)
df["Env"] = df["Tags"].apply(lambda t: t.get("environment", "NON TAGUÉ"))
 
print(df.groupby("Month")["EffectiveCost"].sum())
