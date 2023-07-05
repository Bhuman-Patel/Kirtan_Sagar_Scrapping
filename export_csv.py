# provide name for the output file
output_file = 'gujarati_data.csv'

# this ecoding support's gujarati text in it
encoding = 'utf-8-sig'

# change the name of the df in case it is something else
df.to_csv(output_file, encoding=encoding, index=False)
print(f"Successfully converted Gujarati tabular data to '{output_file}' in CSV format.")