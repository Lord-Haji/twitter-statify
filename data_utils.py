# data_str = "\nCompany  | Time (in years)\nGoogle  | 7 \nFacebook | 8 \nRivian  | 12 \nAmazon   | 16 \nTesla    | 17 \nMicrosoft| 20 \nNetflix  | 21 \nApple    | 30 \nStarbucks| 44 \nMcDonald's| 44 \nNike     | 50 \nDisney   | 74"

# Split the string into lines and remove the header line
def process_data(data_str):
    # Split the string into lines and remove the header line
    # data_str = data_str.replace('\r', '')
    headers = data_str.split('\n')[1].split(',')
    lines = data_str.split('\n')[1:]
    # lines = list(filter(lambda x: x != '', data_str.split('\n')[1:]))
    # print ("lines:")
    # print(lines)

    # Split each line into its company and time fields and save as a list of lists
    data = [[part.strip() for part in line.split(',')] for line in lines]

    col_1 = []
    col_2 = []
    # print("process_data")
    for item in data[1:]:
        col_1.append(item[0])
        col_2.append(int(item[1]))

    return headers[0], headers[1], col_1, col_2


# test = "\nGoogle,7\nFacebook,8\nRivian,12\nAmazon,16\nTesla,17\nMicrosoft,20\nNetflix,21\nApple,30\nStarbucks,44\nMcDonald\u2019s,44\nNike,50\nDisney,74"

# print(process_data(test))