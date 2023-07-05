# Title
title = pd.DataFrame(columns=['category_id', 'sub_category_id', 'kirtan_flag', 'title_name_guj', 'title_name_eng', 'mul_pad_id'])
for index, x in enumerate(df['pad_index']):
    if x == 1:
        # It's required to specify None at each iteration, becuase if there is no value then the variable will contain the value from last iteration
        mul_pad_id = category_id = sub_category_id = title_id = subject_id = kirtan_flag = title_name_guj = title_name_eng = None
        category_id = df.loc[index, 'category_id']
        sub_category_id = df.loc[index, 'sub_category_id']
        #         subject_id = ''
        kirtan_flag = df.loc[index, 'kirtan_flag']
        title_name_guj = df.loc[index, 'title_guj']
        title_name_eng = df.loc[index, 'title_eng']
        mul_pad_id = df.loc[index, 'mul_pad_id']
        new_row = {
            'category_id': category_id,
            'sub_category_id': sub_category_id,
            'kirtan_flag': kirtan_flag,
            'title_name_guj': title_name_guj,
            'title_name_eng': title_name_eng,
            'mul_pad_id': mul_pad_id
        }
        title.loc[len(title)] = new_row
title.sort_values('mul_pad_id', inplace=True)
title.reset_index(inplace=True, drop=True)

title1 = title[['category_id', 'sub_category_id', 'kirtan_flag', 'title_name_guj', 'title_name_eng']]
output_file = 'title.csv'
title1.to_csv(output_file, encoding=encoding, index=False)
print(f"Successfully converted Gujarati tabular data to '{output_file}' in CSV format.")

# Another example of Kirtan Table
# Kirtan
kirtan = pd.DataFrame(
    columns=['category_id', 'sub_category_id', 'pad_id', 'kirtan_url', 'kirtan_guj', 'kirtan_eng'])

# Preparting dict which contains index of all the pads
my_dict = {}
for index, y in enumerate(df['title_guj']):
    my_dict[y] = index

for index, x in enumerate(pad['pad_guj']):
    #     indices = my_dict[x]
    title_id = category_id = sub_category_id = pad_id = subject_id = kirtan_url = kirtan_guj = kirtan_eng = pad_id = None
    kirtan_url = df.loc[index, 'kirtan_url']
    category_id = df.loc[index, 'category_id']
    sub_category_id = df.loc[index, 'sub_category_id']
    title_guj = df.loc[index, 'title_guj']
    kirtan_guj = df.loc[index, 'kirtan_guj']
    kirtan_eng = df.loc[index, 'kirtan_eng']

    new_row = {
        'category_id': category_id,
        'sub_category_id': sub_category_id,
        'pad_id': index + 1,
        'kirtan_url': kirtan_url,
        'kirtan_guj': kirtan_guj,
        'kirtan_eng': kirtan_eng
    }
    kirtan.loc[len(kirtan)] = new_row

for index, x in enumerate(pad['pad_guj']):
    title_id = None
    indices = title.index[title['title_name_guj'] == x].tolist()
    if len(indices) == 1:
        title_id = indices[0]
        mul_pad_id = pad.loc[index, 'mul_pad_id']
        for indexes, y in enumerate(pad['mul_pad_id']):
            if y == mul_pad_id:
                kirtan.loc[indexes, 'title_id'] = title_id + 1
        kirtan.loc[index, 'title_id'] = title_id + 1

output_file = 'kirtan.csv'
kirtan.to_csv(output_file, encoding=encoding, index=False)
print(f"Successfully converted Gujarati tabular data to '{output_file}' in CSV format.")