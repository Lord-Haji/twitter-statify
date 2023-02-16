import matplotlib.pyplot as plt
import seaborn as sns
from data_utils import process_data
from askgpt import spreadify
import random
import string

# Define the data
# data_str= """
# Time it took to reach a $100 billion valuation:

# Google: 7 years
# Facebook: 8 years
# Rivian: 12 years
# Amazon: 16 years
# Tesla: 17 years
# Microsoft: 20 years
# Netflix: 21 years
# Apple: 30 years
# Starbucks: 44 years
# McDonald’s: 44 years
# Nike: 50 years
# Disney: 74 years

# *inflation adjusted
# """

data_str = '''
Universities in the World's Top 100:

🇺🇸 US: 34
🇬🇧 UK: 10
🇩🇪 Germany: 9
🇦🇺 Australia: 7
🇨🇳 China: 7
🇳🇱 Netherlands: 7
🇭🇰 Hong Kong: 5
🇨🇦 Canada: 4
🇫🇷 France:4
🇨🇭 Switzerland: 4
🇰🇷 South Korea: 3
🇯🇵 Japan: 2
🇸🇬 Singapore: 2
🇧🇪 Belgium: 1
🇸🇪 Sweden: 1
'''
def generateplot(data_str):
    title = data_str.split('\n')[1]

    spreadsheet = spreadify(data_str)
    # print(spreadsheet)
    x_title, y_title, names, years = process_data(spreadsheet)

    # Create a plot
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 6))
    palletes = ['YlOrBr', 'PuBuGn', 'BuPu', 'YlOrBr', 'BuGn_r']
    plt.bar(names, years, color=sns.color_palette(random.choice(palletes), len(names)))

    # Set plot title and axis labels
    plt.title(title, fontsize=20, fontweight='bold')
    plt.xlabel(x_title, fontsize=14)
    plt.ylabel(y_title, fontsize=14)

    # Rotate x-axis labels and adjust font size
    plt.xticks(rotation=45, fontsize=12)

    # Remove the top and right spines
    sns.despine(top=True, right=True)

    # Add data labels to the bars
    for i, v in enumerate(years):
        plt.text(i, v + 1, str(v), ha='center', fontsize=12, fontweight='bold')

    # Save the plot as an image

    characters = string.ascii_letters + string.digits
    length = 8
    # Generate a random alphanumeric string of the specified length
    random_string = ''.join(random.choice(characters) for i in range(length))

    plt.savefig('generated.png', bbox_inches='tight')
    print("Plot Generated")

generateplot(data_str)

