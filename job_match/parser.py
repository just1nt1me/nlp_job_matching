from pypdf import PdfReader
import re

#function to process resume and jobl
def get_clean_text(text):
    clean_text = re.sub(r'<[^>]+>', '', text)     # remove html tags
    clean_text = re.sub('http\S+\s*', ' ', clean_text)  # remove URLs
    clean_text = re.sub('RT|cc', ' ', clean_text)  # remove RT and cc
    clean_text = re.sub('#\S+', '', clean_text)  # remove hashtags
    clean_text = re.sub('@\S+', '  ', clean_text)  # remove mentions
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)  # remove punctuations
    clean_text = re.sub(r'[^\x00-\x7f]',r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)  # remove extra whitespace
    clean_text = re.sub(r'(\w)(?<![A-Z])([A-Z])(?![A-Z])', r'\1 \2', clean_text)
    clean_text = clean_text.lower() #remove capital letters
    words = clean_text.split(' ')
    words = [word for word in words if len(word)>1]
    clean_text = ' '.join(words)
    return clean_text

# convert PDFs into a string
def parse_resume(input):
    reader = PdfReader(input)
    number_of_pages = len(reader.pages)
    resume_parts = []

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        clean_text = get_clean_text(text)
        if clean_text:
            resume_parts.append(clean_text)

    resume = ' '.join(resume_parts)
    return resume

def parse_jobl(input):
    reader = PdfReader(input)
    number_of_pages = len(reader.pages)
    jobl_parts = []

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        clean_text = get_clean_text(text)
        if clean_text:
            jobl_parts.append(clean_text)

    jobl = ' '.join(jobl_parts)
    return jobl
