# Gives all the unique value from df column
df1['kirtan_flag'].unique()

# Gives total number of unique values from df column
df1['kirtan_flag'].nunique()

# Reading some of the values from df using slicing method
print(dfs.iloc[5648:6060])

# Getting brief description of df
dfs.info()

# Getting some random sample from df
df.sample()

# Getting count of all the unique values from the df - this will show how many values have how many occurences
df['total_pad'].value_counts()

# Dropping the duplicates
df.drop_duplicates(keep='first',inplace=True,ignore_index=True)

# Replacing values from one df to another using iloc - for mentioning specific index no's
df['kirtan_flag'].iloc[:2101] = df1['kirtan_flag'].iloc[:2101]

# Random Number Generator
number = random.randint(0, 2102)

# Data Type Conversion
df['kirtan_flag'] = df['kirtan_flag'].astype(int)

# Renaming column in df
df.rename(columns={'url':'kirtan_url'},inplace=True)

# Running for loop based on length of list
for x in range(len(dup)):

# Deleting some column from df
result.drop(columns='index', inplace=True)

# Concating multiple df
# Provide name of all the df's in order in a list & use concat()
frames = [dup, org]
result = pd.concat(frames)

# Getting list of index of nan values + Using the value with the help of split()
# First Method
empty_rows = df[df['category_guj'].isna()].index
for x in empty_rows:
    splitter = df.loc[x,'kirtan_url'].split('=')
    last_element = splitter[-1]

# Second Method
empty_rows = df[index(df['category_id'].isnull().tolist())]

# Using Set() for adding only unique and un-ordered value and forming a list out of it
sets = set()
for x in df['SUBJECT']:
    value = x.split(',')
    if len(value) == 1:
        # In case of set - we have to use add(), and in list we have to use append()
        sets.add(value[0])
    else:
        for xx in value:
            sets.add(xx)
len(sets)

# Adding values to dictionary
# Either we can prepare whole list of key-value pair
my_dict = {}
my_dict = {
    '0 R': '૦ 2',
    '0 Pa': '૦ 5'
}
# Alternate way for adding single value
my_dict['PRABHATIYA '] = 'PRABHATIYA'

# Getting content from clipboard and use it
import pyperclip
input_data = pyperclip.paste()

# Using Try-Catch Block for Exception Handling
for index,x in enumerate(dfs['category_guj']):
    key = dfs.loc[index,'category_guj']
    try:
        dfs.loc[index,'catgory_id'] = demo[key]
    except KeyError:
        dfs.loc[index,'catgory_id'] = 0

# Case Conversion of English Text
# Here title() means that only first letter of first word will get capitalised
df['category_eng'] = df['category_eng'].str.upper().str.title()

# Ordering any df into particular order of column
# We can also directly pass the list of cols
cols = ['kirtan_url', 'category_guj', 'category_eng', 'category_id', 'sub_category_guj', 'sub_category_eng','sub_category_id','kirtan_flag','pad_index','title_guj','title_eng','kirtan_guj','kirtan_eng','mul_pad','mul_pad_id']
dfs = dfs[cols]

# Removing specific symbols from data
char_remov = ["!","?",".",",",";",":"]
for char in char_remov:
    string = df['mul_pad'].str.lstrip(char)