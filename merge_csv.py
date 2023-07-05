# Used for working with local files - reading and concating them
import glob
path = '/Users/etechm10/Kirtan-Sagar-Scrapping/Final IPYNB/English Conversion/*.csv'
paths = glob.glob(path)

# this can be used for excluding specific file in from including into the paths variable
paths.remove('/Users/etechm10/Kirtan-Sagar-Scrapping/Last Conversion/kirtan.csv')
paths = sorted(paths)

for file in paths:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)
df.reset_index(inplace=True,drop=True)