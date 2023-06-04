import streamlit as st
from streamlit_chat import message
import complete_prompt

st.set_page_config(
    page_title="ChatUML",
    page_icon=":robot:"
)

st.header("ChatUML")
st.markdown("[Github](https://github.com/ntploc21/ChatUML/)")

# Initialize session state
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! How can I help you today?"]

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ""

if 'diagram' not in st.session_state:
    st.session_state['diagram'] = ""


def get_text():
    '''Get user prompt input'''

    prev_message = ""
    has_prev_message = False
    if (st.session_state['input'] != ""):
        prev_message = st.session_state["input"]
        st.session_state['input'] = ""
        has_prev_message = True

    input_text = st.sidebar.text_input("You: ", key="input")
    if (has_prev_message): input_text = prev_message
    return input_text


user_input = get_text()
if user_input:
    response, diagram = complete_prompt.ask(user_input)

    if diagram:
        st.session_state['diagram'] = diagram

    st.session_state.past.append(user_input)
    st.session_state.generated.append(response)


if st.session_state['diagram']:
    st.image(st.session_state['diagram'], output_format="PNG", use_column_width=True)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        with st.sidebar:
            if (i != len(st.session_state['past'])):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            
            message(st.session_state["generated"][i], key=str(i))
