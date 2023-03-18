
import openai
import os
import getpass

key = getpass.getpass(prompt='Enter your OpenAI API key: ')
openai.api_key = key

