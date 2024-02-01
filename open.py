import openai 

import streamlit as st 

 

OPENAI_API_KEY = '8c91c5c7058847f3820f9d7c12bbb1fb' 

OPENAI_AZURE_ENDPOINT = 'https://sktfly-ai.openai.azure.com/' 

OPENAI_API_TYPE = 'azure' 

OPENAI_API_VERSION = '2023-05-15' 

 

openai.api_key = OPENAI_API_KEY 

openai.azure_endpoint = OPENAI_AZURE_ENDPOINT 

openai.api_type = OPENAI_API_TYPE 

openai.api_version = OPENAI_API_VERSION 

st.title("FLY AI Challenger")

query = st.text_input('Query?: ') 

 

button_result = st.button('RUN') 

 

if button_result: 

    result = openai.chat.completions.create( 

                    model='dev-gpt-35-turbo', 

                    messages=[ 

                        {'role':'system','content':'You are a helpful assitant.'}, 

                        {'role':'user','content':query} 

                    ] 

                ) 

 

    st.write(result.choices[0].message.content) 