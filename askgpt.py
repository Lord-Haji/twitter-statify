import openai
import configparser

# read the config file
config = configparser.ConfigParser()
config.read('secret.ini')


# openai.api_key = "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"

openai.api_key = config.get('API_KEYS', 'openapi_key')


def spreadify(promptstr):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Conver this data to spreadsheet format. Add titles. Use commas to seperate data instead of '|'. Remove units from data eg- years from the second column. Space out every new row with newline. Do not add any data of your own." + promptstr,
    temperature=0.1,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    )
    # print(response)
    # print(response.choices)
    return response.choices[0].text
