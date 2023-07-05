# Loading CSV's into pandas df
# loading dataframe by passing only required columns
df = pd.read_csv('gujarati_data.csv',
                 usecols=['start_index', 'url', 'category_id', 'kirtan_flag', 'pad_index', 'title_guj',
                          'kirtan_guj'])

# Creating New Dataframe from one existing df, by providing only required column names
# pd.DataFrame() -> specifies that it is a type of df
df = pd.DataFrame(columns=['title_guj', 'mul_pad_guj'])