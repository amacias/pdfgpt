from PyPDF2 import PdfReader
#export OPENAI_API_KEY=key_copied_from_openai_site

# This function is reading PDF from the start page to final page
# given as input (if less pages exist, then it reads till this last page)
def get_pdf_text(document_path, start_page=1, final_page=999):
    reader = PdfReader(document_path)
    number_of_pages = len(reader.pages)

    for page_num in range(start_page - 1, min(number_of_pages, final_page)):
        page += reader.pages[page_num].extract_text()
    return page

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
def gpt_req_res(subject_text='write an essay on any subject.',
                prompt_base='answer like an experienced consultant: ',
                model='text-davinci-003',
                max_tokens=1200,
                temperature=0.8):

    # https://platform.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
        model=model,
        prompt=prompt_base + ': ' + subject_text,
        temperature=temperature,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text

doc_path_name = 'test.pdf'
doc_text = get_pdf_text(doc_path_name, 1, 2)
print(doc_text)
#prompt = 'summarize like an experienced consultant in 5 bullets: '
#reply = gpt_req_res(doc_text, prompt)
#print(reply)