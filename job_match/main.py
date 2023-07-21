# Import dependencies

# calculations
import numpy as np
import pandas as pd
# visuals
import matplotlib.pyplot as plt

# parsing and tokenizing
from pypdf import PdfReader
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import re

# similarity score and transfer learning
from scipy import spatial
from absl import logging
import tensorflow as tf
import tensorflow_hub as hub

# import modules
from parser import parse_jobl, parse_resume
from model import load_model, embed

def main(job_listing_file, resume_files):
    # Check file extensions
    if not job_listing_file.endswith('.pdf'):
        raise ValueError("Job listing should be in PDF format")

    for resume_file in resume_files:
        if not resume_file.endswith('.pdf'):
            raise ValueError(f"{resume_file} should be in PDF format")

    # 1. Load and parse job listing
    jobl = parse_jobl(job_listing_file)
    print("Job Listing PDF contents parsed")
    # print("*"*20)
    # print(jobl)

    # 2. Load model and create the job embedding
    model = load_model()
    job_embedding = embed(model, jobl)

    # Create a list to store the results
    results = []

    for resume_file in resume_files:
        # 3. Load and parse resume
        resume = parse_resume(resume_file)
        print("Resume PDF contents parsed")
        # print("*"*20)
        # print(resume)

        # 4. Create the resume embedding
        resume_embedding = embed(model, resume)

        # 5. Calculate Similarity Score
        similarity_score = 1 - spatial.distance.cosine(job_embedding, resume_embedding)

        # Append the result to the list
        results.append({
            'Resume': resume,
            'Job Listing': jobl,
            'Similarity Score': similarity_score
        })

    # Create a DataFrame from the results list
    df = pd.DataFrame(results).sort_values(by='Similarity Score', ascending=False)

    print(df)

if __name__ == '__main__':
    # job_listing_file = '../files/CTW Data Scientist.pdf'
    # job_listing_file = '../files/nova_jl.pdf'
    job_listing_file = '../files/PayPay _software_dev_engineer.pdf'
    resume_files = ['../files/resume.pdf', '../files/jack_merret_resume.pdf', '../files/jon_nogueira_resume.pdf', '../files/jon_nog_jap_resume.pdf']
    main(job_listing_file, resume_files)
