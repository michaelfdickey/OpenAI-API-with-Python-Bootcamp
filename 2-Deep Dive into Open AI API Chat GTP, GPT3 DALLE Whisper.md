# Deep Dive into Open AI, ChatGPT, GPT-3, DALL-E, Whisper

## 2-1: Create an OpenAI Account and an OpenAI API key

![image-20230317214946711](./../../../../../MFD Personal/Programming/python/Udemy/OpenAI API with Python Bootcamp/image-20230317214946711.png)

To use the AI models by OpenAI, create an account and create an OpenAI API key

Login https://platform.openai.com/

![image-20230317215352678](./../../../../../MFD Personal/Programming/python/Udemy/OpenAI API with Python Bootcamp/image-20230317215352678.png)

## 2-2: Installing OpenAI API library and Authenticating

two native and officially supported API for python

![image-20230317220124556](./../../../../../MFD Personal/Programming/python/Udemy/OpenAI API with Python Bootcamp/image-20230317220124556.png)

```
import openai
```

 To run a command in jupyter notebook prefix it with `!`

![image-20230317220710709](./image-20230317220710709.png)



You'll need to auth with the API key and should store it as an env var

In jupyter notebook to create environment variables to store API key

![image-20230317221108494](./image-20230317221108494.png)

to retrieve the value:

```
os.getenv('x')
```

![image-20230317221201357](./image-20230317221201357.png)

```
os.environ['OPENAI_API_KEY'] = 'key_in_clear_text'
openai.api_key = os.getenv('OPENAI_API_KEY')
```

instead of pasting it in clear text, you can prompt for it as input

![image-20230317221518581](./image-20230317221518581.png)



# 2-7: Open AI Models

Ok we now have an OpenAI account and an OpenAI API key

let's strart making requests to the open API models

but lets first talk about them

An AI model is a software program that uses specific ML and DL algorithms and has been trained on a set of data to perform specific tasks

ML  - machine learning

DL - deep learning

Models https://platform.openai.com/docs/models



![image-20230317222502773](./image-20230317222502773.png)

Pricing:

openai.com/pricing

You can use the playground to compare models

https://platform.openai.com/playground



# 2-8: Making GPT-3 Requests Using the OpenAI API

now you'll learn how to make your applciation talk to openAPI models

create the prompt

prompt engineering

forums / discords / cheat sheets

deeper into this in another video

we're going to use davinci

the prompt is the most important part

Example:

```
openai.Completion.create()              # will take some paramaters and return a response object
response = openai.Compeltion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
)
```

choose your models, these can change. 

![image-20230317230557393](./image-20230317230557393.png)

