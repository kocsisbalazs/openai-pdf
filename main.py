import os
import Pypdf2   
from openai import OpenAI
from dotenc import find_dotenv, load_dotenv
import prompts


# Load the environment 
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

model = "gpt-3.5-turbo"
temperature = 0.3
max_tokens = 500


# Reading the book pdf
book = ""
file_path = "book.pdf"
with open(file_path, "rb") as file:
    pdf = PyPDF2.PdfFileReader(file)
    for page in pdf.pages:
        book += pdf.extractText()
        start_page = 23
        end_page = 100

messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": prompt}
]



# Prompting the model
system_message = prompts.system_message()
prompt = prompts.book_prompt(book, system_message)

def get_summary():
    completion = client.chat.completetions.create(
        model = model,
    )