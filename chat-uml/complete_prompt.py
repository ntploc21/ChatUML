import openai
import streamlit as st
import json
import uml_generate

openai.api_key = st.secrets["OPENAI_API_KEY"]


# @st.experimental_memo
def load_initial_prompt():
    prompt_list = json.load(open('prompts/initial_prompt.json', 'r'))
    return prompt_list


raw_chat_message = load_initial_prompt()


def error():
    return '''Sorry, I don't know which diagram to generate with that information you gave me.
                    You can try to customize your prompt to be like this example:
                    \"Can you generate for me a simple compiler diagram?\"''', False


def ask(user_message):
    raw_chat_message.append({"role": "user", "content": user_message})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=raw_chat_message,
        temperature=0.2,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    response_content = response['choices'][0]['message']['content']
    uml_diagram_start_idx = response_content.find("@startuml")

    if (uml_diagram_start_idx == -1):
        return error()
    description_response = response_content[:uml_diagram_start_idx].strip()
    uml_diagram_code_response = response_content[uml_diagram_start_idx:]

    raw_chat_message.append({"role": "assistant", "content": response_content})

    uml_diagram = uml_generate.get_uml_diagram(uml_diagram_code_response)
    if (uml_diagram == ""):
        return error()

    return description_response, uml_diagram