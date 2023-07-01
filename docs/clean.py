import pandas as pd
import numpy as np

df_l = pd.read_csv("databases/life.csv")
df_c = pd.read_csv("databases/country-data.csv")

# df country data
df_c = df_c[df_c['year'] == 2016]
df_c = df_c.drop(['year', 'Unnamed: 0'], axis=1)
df_c = df_c.rename(columns={"alpha-3": "country_code", "name": "country", "Population": "population"})
df_c = df_c.fillna(-1)
df_c = df_c.reset_index()
df_c = df_c.drop('index', axis=1)

# df life data
df_l = df_l[df_l['year'] == 2016]
cols_to_keep = [col for col in df_l.columns if not any(word in col for word in ['une'])]
df_l = df_l[cols_to_keep]
df_l = df_l.drop(['year','che_gdp', 'doctors', 'gghe-d', 'region'], axis=1)
df_l = df_l.dropna(axis=1, how='all')
df_l = df_l.fillna(-1)
df_l = df_l.reset_index()
df_l = df_l.drop('index', axis=1)

# aggregate nieuwe columns voor capita
# skip alle data waarbij -1 optreed
df_c['CO2_per_capita'] = np.where((df_c['population'] != -1)  & (df_c['CO2'] != -1), (df_c['CO2'] / df_c['population']) * 1000, -1)
df_c['GDP_per_capita'] = np.where((df_c['population'] != -1) & (df_c['GDP'] != -1), df_c['GDP'] / df_c['population'], -1)
df_l['age5-19healthyweight'] = np.where((df_l['age5-19thinness'] != -1) & (df_l['age5-19obesity'] != -1),
                                            100 - df_l['age5-19thinness'] - df_l['age5-19obesity'], -1)
df_l['adult_mortality'] = df_l['adult_mortality'] / 10

# merge data en maak nieuwe 
merged_df = df_c.merge(df_l, on='country_code')
merged_df = merged_df.drop('country_y', axis=1)
merged_df = merged_df.rename(columns={"country_x": "country"})
merged_df.to_csv("databases/merged.csv", index=False)