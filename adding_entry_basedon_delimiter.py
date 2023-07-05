# In this case, there are various comma separated values and for each of the value I want new row
# I can use comma as delimiter and if there is no comma in the string then there are two case
# either there is only 1 value else the cell is NULL
# I have used isdigit() for confirming that the single value is Int and else I don't have to add the value, as it is NULL

multiple_krt1 = pd.DataFrame(columns=['topics_id','title_guj'])
for index,x in enumerate(multiple_krt['topics_id']):
    # specifying the delimiter
    commais = ','
    if commais in str(x):
        splitss = str(x).split(',')
        for z in splitss:
            topics_id = z
            title_guj = multiple_krt.loc[index,'title_guj']
            new_row = {
                    'topics_id': topics_id,
                    'title_guj': title_guj,
                }
            multiple_krt1.loc[len(multiple_krt1)] = new_row
            topics_id = None
            title_guj = None
    else:
        if str(x).isdigit():
            topics_id = multiple_krt.loc[index,'topics_id']
            title_guj = multiple_krt.loc[index,'title_guj']
            new_row = {
                    'topics_id': topics_id,
                    'title_guj': title_guj,
                }
            topics_id = None
            title_guj = None
            multiple_krt1.loc[len(multiple_krt1)] = new_row