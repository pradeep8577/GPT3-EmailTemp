import os
import openai
from werkzeug.wrappers import response
import config

openai.api_key = config.OPENAI_API_KEY

def generateBlogTopics(prompt1):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Write a cold email to potential clients about: {}.".format(prompt1),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response['choices'][0]['text']

