# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from streamlit_option_menu import option_menu

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
myOpenAIkey = os.getenv("my_OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = myOpenAIkey

# Initialize OpenAI language model
llm = OpenAI(temperature=0.4)

# Define Prompt Template for generating cover letters
In_Put_Template = PromptTemplate(
    input_variables=["input_CV", "input_JobDescription"],
    template=""" Based on the 
                 resume here: {input_CV} and job description here: {input_JobDescription} write effective cover letter
                  for the job."""

)

# Function to clear history
def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']





# Display custom CSS
st.markdown('<style>' + open('wave.css').read() + '</style>', unsafe_allow_html=True)

# Main content of the application
st.image("Abank.webp", width=120)  # Logo or main image
st.title("Cover Letter Generator")  # Title

# Text areas for input with custom styling
with st.sidebar:
    st.write("")  # Empty space to separate sidebar content

input_CV = st.text_area("Paste your resume or CV here:", height=200)  # Text area for CV input
input_JobDescription = st.text_area("Paste the Job Description here:", height=200)  # Text area for Job Description input

# Button to generate cover letter with custom styling
Button_Click = st.button("Create Cover Letter", on_click=clear_history, key="create_button", help="Button that will generate the cover letter.")

# Handling button click event
if Button_Click:
    response = llm(In_Put_Template.format(input_CV=input_CV, input_JobDescription=input_JobDescription))
    st.subheader("Generated Cover Letter")
    st.text_area("Scrolling text container:", value=response, height=400)
# Image Design

with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Projects", "Contact"],
            icons=["house","book","envelope"]

        )
#if selected == "Home":
#    st.title(f"You have selected {selected}")
#if selected == "Home":
#    st.title(f"You have selected {selected}")
#if selected == "Home":
#    st.title(f"You have selected {selected}")

# Footer or additional information section
st.sidebar.title('About')
st.sidebar.info(
    "This application generates a cover letter based on your resume or CV and the job description provided. "
    "It uses OpenAI's language model to create an effective cover letter."
)
