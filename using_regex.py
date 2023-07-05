import re

# First Method
pattern = r'/.{1,}'
replacement = '...'
text = df.loc[index, 'kirtan_eng']
df.loc[index, 'kirtan_eng'] = re.sub(pattern, replacement, text)

# Second Method
pattern = r'pattern_to_match'
replacement = 'replacement_text'

# Perform the replacement on the 'lyrics' column
df['lyrics'] = df['lyrics'].str.replace(pattern, replacement)
print(df)

# Searching and Getting the value based on regex
pad_index = re.search(r'(\d+)/', title_guj)
pad_index_element = pad_index.groups(1)
df.loc[index,'pad_index'] = pad_index_element[0]