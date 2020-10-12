# Simple ETL process for a basic home expenses table

# Import pandas and read the csv where the expenses are (downloaded from your bank)
import pandas as pd
gastos_sin_editar = pd.read_csv('datasets/gastos.csv', sep=";", decimal = ",", dayfirst = True)

# Keeping the relevant columns
gastos2=gastos_sin_editar[["Fecha_Valor","Concepto","Importe"]]

# Changing the name of the columns using a dictionary
gastos2 = gastos2.rename(columns={"Fecha_Valor":"DATE", "Concepto":"CONCEPT", "Importe":"IMPORT"})

# Adding a new column in case observations are needed
gastos2.loc[:,"OBSERVATION"] = 'NaN'

# Creating and performing boolean masks filtering
mask = gastos2['IMPORT'] > 0
gastos2.loc[mask, 'CLASS'] = 'Income'
gastos2.loc[~mask, 'CLASS'] = 'Expense'

mask = gastos2['CONCEPT'].str.lower().str.find('pepe mobil') >= 0
gastos2.loc[mask, 'TYPE'] = 'Phone'
gastos2.loc[mask, 'SUBTYPE'] = 'Pablo'

mask = gastos2['CONCEPT'].str.lower().str.find('yoigo') >= 0
gastos2.loc[mask, 'TYPE'] = 'Phone'
gastos2.loc[mask, 'SUBTYPE'] = 'Nilu'

mask = gastos2['CONCEPT'].str.lower().str.find('consum') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Groceries'

mask = gastos2['CONCEPT'].str.lower().str.find('just-eat') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Delivery'

mask = gastos2['CONCEPT'].str.lower().str.find('dominos pizza') >= 0
gastos2.loc[mask, 'TYPE'] = 'Food'
gastos2.loc[mask, 'SUBTYPE'] = 'Delivery'

mask = gastos2['CONCEPT'].str.lower().str.find('farmacia') >= 0
gastos2.loc[mask, 'TYPE'] = 'Pharmacy'

mask = gastos2['CONCEPT'].str.lower().str.find('ecooltra') >= 0
gastos2.loc[mask, 'TYPE'] = 'Movility'
gastos2.loc[mask, 'SUBTYPE'] = 'Motorbike'

mask = gastos2['CONCEPT'].str.lower().str.find('taxi') >= 0
gastos2.loc[mask, 'TYPE'] = 'Movility'
gastos2.loc[mask, 'SUBTYPE'] = 'Motorbike'

mask = gastos2['IMPORT'] = 675
gastos2.loc[mask, 'TYPE'] = 'Rental'

# Exporting the results to a new dataset to be visualized
gastos2.to_csv('datasets/gastos_editado.csv', sep=";", decimal = ",", date_format = '%Y/%m/%d')
