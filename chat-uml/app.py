import streamlit as st
from streamlit_chat import message
import complete_prompt

st.set_page_config(
    page_title="ChatUML",
    page_icon=":robot:"
)

st.header("ChatUML")
st.markdown("[Github](https://github.com/ntploc21/ChatUML/)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! How can I help you today?"]

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ""


def get_text():
    """Get user input"""

    prevMessage = ""
    hasPrevMessage = False
    if (st.session_state['input'] != ""):
        prevMessage = st.session_state["input"]
        st.session_state['input'] = ""
        hasPrevMessage = True

    input_text = st.sidebar.text_input("You: ", key="input")
    if (hasPrevMessage): input_text = prevMessage
    return input_text


user_input = get_text()

if user_input:
    # output = query({
    #     "inputs": {
    #         "past_user_inputs": st.session_state.past,
    #         "generated_responses": st.session_state.generated,
    #         "text": user_input,
    #     },"parameters": {"repetition_penalty": 1.33},
    # })

    response, success = complete_prompt.ask(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(response)


if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        with st.sidebar:
            if (i != len(st.session_state['past'])):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            
            message(st.session_state["generated"][i], key=str(i))
