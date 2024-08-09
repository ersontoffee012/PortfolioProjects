#Data Cleaning in Pandas

import pandas as pd

df = pd.read_excel(r"C:\Users\Toffee\OneDrive\Documents\Data Analyst\Python Pandas Adventure\Customer Call List.xlsx")
df

# Removing Duplicates

df = df.drop_duplicates()
df

# Removing Columns

df = df.drop(columns = "Not_Useful_Column")
df

# Strip: it takes either the lstrip left side or the rstrip right side and strip takes from both
# Cleaning Names

#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")
df

# Cleaning Phone Numbers

#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','',regex=True)
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
#df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# Cleaning Addresses
# Splitting Columns

df[["Street Address", "State", "Zip"]] = df["Address"].str.split(',', n=2, expand=True)
df

# Cleaning DNC and Paying Customer

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df

#df = df.replace('N/a','')
#df = df.replace('NaN','')

#df = df.fillna('')
df

# Filtering Row Data

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
df

for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
df

#Another way to drop Null Values

#df = df.dropna(subset="Phone_Number", inplace=True)

df = df.reset_index(drop=True)
df


