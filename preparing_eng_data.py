# First provide all the combination which can be occured for the change
my_dict = {
    'VIRAH-VEDNA' : 'VIRAH',
    'VINANTI' : 'PRARTHANA',
    'PRARTHANA' : 'PRARTHANA',
    'ARJI' : 'PRARTHANA',
    'DINTA' : 'DASATVA',
    'PREMBHAKTI' : 'PREMBHAKTI',
    'MURTIVARNAN' : 'MURTI',
    'PADHARAMNI' : 'PADHARAMANI',
    'UPDESH' : 'UPDESH',
    'BHAGWAD MAHIMA' : 'MAHIMA',
    'BAL LILA' : 'BALKIRTAN',
    'STUTI' : 'STUTI'
}
for index,x in enumerate(df['CATEGORY']):
    for y in x.split(' '):
        if my_dict.has_key(x):
            value = df.loc[index,'NEW_CATEGORY']
            if value == '':
                df.loc[index,df['NEW_CATEGORY']] = my_dict[y]