import pandas as pd

df = pd.read_csv("online_store_data.csv")

df['rating'] = df['rating'].str.extract(r'(\d+\.?\d*)')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['quantity_sold'] = pd.to_numeric(df['quantity_sold'], errors='coerce')
df['quantity_in_stock'] = pd.to_numeric(df['quantity_in_stock'], errors='coerce')

#1. prosecna ocena proizvoda u online trgovini
prosecna_ocena = df['rating'].mean()
print(f"1. Prosecna ocena proizvoda: {prosecna_ocena:.2f}")

#2. najcesci brend u online trgovini
najcesci_brend = df['brand'].mode()[0]
print(f"2. Najcesci brend: {najcesci_brend}")

#3. najprodavaniji brend u online trgovini
najprodavaniji = df.groupby('brand')['quantity_sold'].sum().idxmax()
print(f"3. Najprodavaniji brend: {najprodavaniji}")

#4.  prosecna ocena proizvoda po kategorijama
prosecna_ocena_po_kategoriji = df.groupby('category')['rating'].mean()
print("4. Prosecna ocena po kategorijama:")
print(prosecna_ocena_po_kategoriji)

#5. popularnost proizvoda po bojama
popularnost_po_bojama = df.groupby('color')['quantity_sold'].sum().sort_values(ascending=False)
print("5. Popularnost po bojama (broj prodatih proizvoda):")
print(popularnost_po_bojama)

#6. 5 najefikasnijih brendova po pitanju prodaje
efikasnost = df.groupby('brand').agg({
    'quantity_sold': 'sum',
    'quantity_in_stock': 'sum'
})
efikasnost['efficiency'] = efikasnost['quantity_sold'] / (efikasnost['quantity_sold'] + efikasnost['quantity_in_stock'])
top5_efikasnih = efikasnost.sort_values(by='efficiency', ascending=False).head(5)
print("6. Top 5 najefikasnijih brendova po prodaji:")
print(top5_efikasnih[['efficiency']])
