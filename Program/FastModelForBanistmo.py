#Preliminary python program to answer the banistmo challenge in a few hours because I didn't have much time. 
# Developed by David Martínez

# Convert `fecha_var_rpta_alt` to datetime
df_base_pivot_oot['fecha_var_rpta_alt'] = pd.to_datetime(df_base_pivot_oot['fecha_var_rpta_alt'], format='%Y%m')

# Show the updated df.info() output
print("\ndf_base_pivot_oot.info() after converting to datetime:")
print(df_base_pivot_oot.info())

# Print the number of rows and columns in each dataframe
dataframes = {
    'df_base_pivot_trtest': df_base_pivot_trtest,
    'df_probabilidad_oblig': df_probabilidad_oblig,
    'df_master_customer': df_master_customer,
    'df_maestra_cuotas_pagos': df_maestra_cuotas_pagos,
    'df_base_pivot_oot': df_base_pivot_oot
}

for df_name, df in dataframes.items():
    print(f"\nShape of {df_name}: {df.shape}")

# Print the percentage of missing values for each column in each dataframe
for df_name, df in dataframes.items():
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    print(f"\nPercentage of missing values in {df_name}:")
    print(missing_percentage[missing_percentage > 0].to_markdown(numalign="left", stralign="left",floatfmt='.2f'))

# Print the number of unique values and the most frequent values for each categorical column in each dataframe
for df_name, df in dataframes.items():
    print(f"\nUnique values and most frequent values for categorical columns in {df_name}:")
    for col in df.select_dtypes(include='object'):
        print(f"\nColumn: {col}")
        print(f"Number of unique values: {df[col].nunique()}")
        print(f"Most frequent value: {df[col].value_counts().index[0]}")

# For the df_base_pivot_trtest dataframe
# Print descriptive statistics for numeric columns
print("\nDescriptive statistics for numeric columns in df_base_pivot_trtest:")
print(df_base_pivot_trtest.describe().to_markdown(numalign="left", stralign="left"))

# Print the distribution of the target variable var_rpta_alt
print("\nDistribution of the target variable 'var_rpta_alt' in df_base_pivot_trtest:")
print(df_base_pivot_trtest['var_rpta_alt'].value_counts().to_markdown(numalign="left", stralign="left"))

# For the df_maestra_cuotas_pagos dataframe
# Group the data by nit_enmascarado and num_oblig_enmascarado and count the number of rows
grouped_data = df_maestra_cuotas_pagos.groupby(['nit_enmascarado', 'num_oblig_enmascarado']).size().to_frame(name='count')

# Print descriptive statistics of this count
print("\nDescriptive statistics of the count of rows per (nit_enmascarado, num_oblig_enmascarado) in df_maestra_cuotas_pagos:")
print(grouped_data.describe().to_markdown(numalign="left", stralign="left"))

# For the df_master_customer dataframe
# Print the number of unique values for nit_enmascarado
print(f"\nNumber of unique values for 'nit_enmascarado' in df_master_customer: {df_master_customer['nit_enmascarado'].nunique()}")

# Group the data by nit_enmascarado and count the number of rows
grouped_data_customer = df_master_customer.groupby(['nit_enmascarado']).size().to_frame(name='count')

# Print descriptive statistics of this count
print("\nDescriptive statistics of the count of rows per 'nit_enmascarado' in df_master_customer:")
print(grouped_data_customer.describe().to_markdown(numalign="left", stralign="left"))

# For the df_probabilidad_oblig dataframe
# Group the data by nit_enmascarado and num_oblig_enmascarado and count the number of rows
grouped_data_prob = df_probabilidad_oblig.groupby(['nit_enmascarado', 'num_oblig_enmascarado']).size().to_frame(name='count')

# Print descriptive statistics of this count
print("\nDescriptive statistics of the count of rows per (nit_enmascarado, num_oblig_enmascarado) in df_probabilidad_oblig:")
print(grouped_data_prob.describe().to_markdown(numalign="left", stralign="left"))

# Print the time range in fecha_corte for each of df_probabilidad_oblig and df_maestra_cuotas_pagos dataframes
print(f"\nTime range in 'fecha_corte' for df_probabilidad_oblig: {df_probabilidad_oblig['fecha_corte'].min()} to {df_probabilidad_oblig['fecha_corte'].max()}")
print(f"\nTime range in 'fecha_corte' for df_maestra_cuotas_pagos: {pd.to_datetime(df_maestra_cuotas_pagos['fecha_corte'], format='%Y%m%d').min()} to {pd.to_datetime(df_maestra_cuotas_pagos['fecha_corte'], format='%Y%m%d').max()}")

# Print the time range in fecha_var_rpta_alt for df_base_pivot_trtest dataframe
print(f"\nTime range in 'fecha_var_rpta_alt' for df_base_pivot_trtest: {df_base_pivot_trtest['fecha_var_rpta_alt'].min()} to {df_base_pivot_trtest['fecha_var_rpta_alt'].max()}")

# Print the time range in fecha_var_rpta_alt for df_base_pivot_oot dataframe
print(f"\nTime range in 'fecha_var_rpta_alt' for df_base_pivot_oot: {df_base_pivot_oot['fecha_var_rpta_alt'].min()} to {df_base_pivot_oot['fecha_var_rpta_alt'].max()}")
