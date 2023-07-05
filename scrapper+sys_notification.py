class system_notification:
    # functions's used to get system notification based on the IPYNB file's cell execution status
    # providing system notification when the cell has completed execution

    def notify_completion():
        title = 'Cell Execution Completed'
        subtitle = 'The cell has finished executing'
        script = f'display notification "{subtitle}" with title "{title}" sound name "default"'
        subprocess.run(['osascript', '-e', script])

    # providing system notification based on custom logic
    def notify_status(status):
        title = 'Reached Milestone:'
        subtitle = 'Working on it, further'
        script = f'display notification "{subtitle}" with title "{title} : {status}" sound name "default"'
        subprocess.run(['osascript', '-e', script])

    # providing system notification when the cell has thrown exception while running the code
    def notify_error(exception):
        title = 'Error in Cell Execution'
        error_message = str(exception)
        script = f'display notification "{error_message}" with title "{title}" sound name "default"'
        subprocess.run(['osascript', '-e', script])


# scrapper function = Used for getting all the data from the website and also formatting it
def scrapper(start_index: int, end_index: int):
    try:
        while (start_index != end_index):
            # url
            url = f'http://www.swaminarayankirtan.org/Kirtan_Display.aspx?Kid={start_index}'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            mul_pad_element = soup.find(id="ctl00_ContentPlaceHolder1_tdKirtanPadBody")
            if mul_pad_element is not None:
                heading_guj = soup.find(id="ctl00_ContentPlaceHolder1_tdKirtanName").text
                mul_pad = soup.find(id='ctl00_ContentPlaceHolder1_tdKirtanPadBody').text
                all_val = heading_guj.split('/')
                guj_title = all_val[0][:-1]
                new_row = {
                    'title_guj': title_guj,
                    'mul_pad': mul_pad
                }
                print(start_index)
                df.loc[len(df)] = new_row
                poet = soup.find(id="ctl00_ContentPlaceHolder1_tdKirtanGayakBody")
                if poet is not None:
                    poet = poet = soup.find(id="ctl00_ContentPlaceHolder1_tdKirtanGayakBody").text
                else:
                    poet = ''
                lyrics_guj = soup.find(id="ctl00_ContentPlaceHolder1_tdKirtan").text

                html_plain_text = lyrics_guj.replace('\r', "").replace('\t', "    ").replace("'r", "").replace("r'",
                                                                                                               "").replace(
                    "\xa0", "")

                temp_lyr = []
                for index, i in enumerate(html_plain_text.split("\n")):
                    if (index == 0):
                        repair = i.lstrip()
                        temp_lyr.append(repair)
                    else:
                        if (i != ''):
                            temp_lyr.append(i)

                lyrics_temp = []
                for line in temp_lyr:
                    if (line != ''):
                        lyrics_temp.append(line)
                print(lyrics_temp)

                first_pos = lyrics_temp[0].startswith("પદ")
                if (first_pos):
                    lyrics_temp = lyrics_temp[1:]
                else:
                    lyrics_temp = lyrics_temp[0:]
                lyrics_guj = '\n'.join(lyrics_temp)
                title_guj = guj_title.replace('.', '').replace(';', '').replace(':', '').strip()

                # Logic for converting gujarati digits to english
                guj_eng = {'૦': '0', '૧': '1', '૨': '2', '૩': '3', '૪': '4', '૫': '5', '૬': '6', '૭': '7', '૮': '8',
                           '૯': '9'}
                guj_pad = all_val[0][-1]
                pad_index = guj_eng.get(guj_pad)

                # Adding value to kirtan_flag column based on total_pad
                if (total_pad == 1):
                    kirtan_flag = 0
                else:
                    kirtan_flag = 1

                # adding new row in df is easy when preparing dictionary for it
                new_row = {
                    'start_index': start_index,
                    'url': url,
                    'category_id': poet,
                    'kirtan_flag': kirtan_flag,
                    'pad_index': pad_index,
                    'title_guj': title_guj,
                    'mul_pad': mul_pad,
                    'kirtan_guj': lyrics_guj
                }
                df.loc[len(df)] = new_row
                print(df)

        if (start_index % 1000 == 0):
            notify_status(start_index)

        start_index += 1
    except Exception as e:
        start_rows = df.shape[0]

    # This will auto-start the script again from where it is stopped, this way there will be no need to resume the cell manually
    if start_rows <= 17476:
        diff = 17476 - start_rows
        if diff > 100:
            end_rows = start_rows + 100


# running scrapper function
scrapper(start_rows + 1, end_rows)
notify_error(e)
scrapper(0, 17476)
notify_completion()
