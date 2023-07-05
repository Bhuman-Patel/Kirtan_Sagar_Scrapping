# this type of absolute path can also be given when the script file is not in the same folder as that of csv file
path = '/Users/etechm10/Kirtan-Sagar-Scrapping/Final IPYNB/cleared_final_master.csv'

subject = pd.read_csv(f'{path}',usecols=['kirtan_url','topics_eng','title_guj'])
convertor = {'AASHARO': 'આશરો',
             'BAL KIRTAN': 'બાળ કીર્તન',
             'DASATVA': 'દાસત્વ',
             'DHYAN': 'ધ્યાન',
             'DHYEY': 'ધ્યેય',
             'KARUNA': 'કરુણા',
             'LILA BHAKTI': 'લીલા ભક્તિ',
             'MAHIMA': 'મહિમા',
             'MURTI': 'મૂર્તિ',
             'NISHTHA': 'નિષ્ઠા',
             'NITYA NIYAM': 'નિત્ય નિયમ',
             'PADHARAMANI': 'પધરામણી',
             'PODHANIYA': 'પોઢણીયા',
             'PRABHATIYA': 'પ્રભાતિયા',
             'PRARTHANA': 'પ્રાર્થના',
             'PREM BHAKTI': 'પ્રેમ ભક્તિ',
             'SHRADDHANJALI': 'શ્રદ્ધાંજલિ',
             'STUTI': 'સ્તુતિ',
             'UPDESH': 'ઉપદેશ',
             'UTSAV': 'ઉત્સવ',
             'VIRAH': 'વિરહ',
             'YUVA KIRTAN': 'યુવા કીર્તન',
             'DOHA-CHHAND': 'દોહા-છંદ'}

for index, x in enumerate(df['topics_eng']):
    temp_var = str(x)
    for y in convertor:
        # simply replace every value of the cell with the corresponding values from the dict based on the key
        temp_var = temp_var.replace(y, convertor[y])
    df.loc[index, 'topics_guj'] = temp_var

    # we can get only selected columns from any df by using this type of [[ (double square braces)
    # this is also useful in case we want to sort the column values, in some specific order
    subject = subject[['images', 'topics_guj', 'topics_eng']]