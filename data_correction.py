my_dict = {
    '0 R': '૦ 2',
    '0 Pa': '૦ 5',
    '0 P': '૦ 5',
    '2khe0': 'Rakhe',
    'ઽ': ';',
    'Teka': 'Tek',
    '-\n': ',\n',
    '2khe0 ': '',
    'X': '?',
    'DuઃKh': 'Dukh',
    'Dunykha': 'Dukh',
    'DuઃKhiya': 'Dukhiya',
    'NiઃShank': 'Nishank',
    'Valama': 'Valama',
    'Prataઃ': 'Pratah',
    '0 ': '૦ ',
    'â€¦': '...',
    '?\n': ';\n',
    'Jigyanja': 'Gyan',
    'Lejar-': 'Ler,',
    'Lejar': 'Ler',
    'Gayajata': "Gayata",
    'Kejadada': 'Kedada',
    'Rejashu': 'Reshu',
    'Lavyajata': 'Lavyata',
    'Nojatu': 'Notu',
    'Najava': 'Nava',
    'Pejari': 'Peri',
    'Mejar': 'Mer',
    'Kahijati': 'Kahiti',
    'Najave': 'Nave',
    'Gaijati': 'Gaiti',
    "'Ta": "ta",
    'Sanj,Savare': 'Sanj-Savare',
    'Tan,Man,Dhan': 'Tan-Man-Dhan',
    'Tan,Man': 'Tan-Man',
    'Tan,Dhan': 'Tan-Dhan',
    'Prem,Adhar,Ras': 'Prem-Adhar-Ras',
    'Sukh,Dukh': 'Sukh-Dukh',
    'Mat,Pita': 'Mat-Pita',
    'Santo,Bhakto': 'Santo-Bhakto',
    '���Ub ': ' ',
    'La���Shu': 'Lavshu',
    '…R': '...2',
    '…P': '...5',
    '…': '...',
    '\n ': '\n',
    '\n    ': '\n     ',
    '? \n': '; \n',
    ' - ': '...',
    '5ri': 'pri',
    '-\n': ',\n',
    '- \n': ', \n',
    '...5': '...P',
    '...2': '...R',
    '...R \n': '...2 \n',
    '...P \n': '...5 \n',
    '...R\n': '...2\n',
    '...P\n': '...5\n',
    '5rabhumaro': 'Prabhumaro',
    '        -': '...',
    '    -': '...',
    '- ': ', ',
    'Chhandany': 'Chhand:'
}
# For Kirtan Lyrics
for index, x in enumerate(df['kirtan_eng']):
    for y in my_dict:
        before = y
        after = my_dict[y]
        df.loc[index, 'kirtan_eng'] = df.loc[index, 'kirtan_eng'].replace(before, after)

# 2nd
lst = [' Na', ' Naa', ' Ni', ' Nee', ' Nu', ' Noo', ' Ne', ' Nai', ' No', ' Nau', ' Nam', ' Nah', ' Tha', ' Thaa',
       ' Thi', ' Thee', ' Thu', ' Thoo', ' The', ' Thai', ' Tho', ' Thau', ' Tham', ' Thah', ' Ma', ' Maa', ' Mi',
       ' Mee', ' Mu', ' Moo', ' Me', ' Mai', ' Mo', ' Mau', ' Mam', ' Mah']
lsts = ['na', 'naa', 'ni', 'nee', 'nu', 'noo', 'ne', 'nai', 'no', 'nau', 'nam', 'nah', 'tha', 'thaa', 'thi', 'thee',
        'thu', 'thoo', 'the', 'thai', 'tho', 'thau', 'tham', 'thah', 'ma', 'maa', 'mi', 'mee', 'mu', 'moo', 'me',
        'mai', 'mo', 'mau', 'mam', 'mah']

for index, x in enumerate(lst):
    pattern = fr'\b{lst[index]}\b'
    replacement = lsts[index]
    df['kirtan_eng'] = df['kirtan_eng'].str.replace(pattern, replacement)

# 3rd
letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', '(11)', '(12)', '(13)',
           '(14)', '(15)', '(16)', '(17)', '(18)', '(19)', '(20)']
for index, x in enumerate(df['kirtan_eng']):
    for z in letters:
        first = f'-{str(z)}'
        second = f'૦ {z}'
        df.loc[index, 'kirtan_eng'] = df.loc[index, 'kirtan_eng'].replace(first, second)


# In case we need to perform some correction of some specific value in particular df column
for index,x in enumerate(df['lyrics']):
    before = '\n   ૦ '
    after = '\n     '
    df.loc[index,'lyrics'] = df.loc[index,'lyrics'].replace(before, after)