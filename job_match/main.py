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

# similarity score
from scipy import spatial
from absl import logging
import tensorflow as tf
import tensorflow_hub as hub

# import modules
from parser import parse_jobl, parse_resume
from model import embed

def main(job_listing_file, resume_file):
    # Check file extensions
    if not job_listing_file.endswith('.pdf'):
        raise ValueError("Job listing should be in PDF format")
    if not resume_file.endswith('.pdf'):
        raise ValueError("Resume should be in PDF format")

    # 1. Load and parse job listings and resumes
    jobl = parse_jobl(job_listing_file)
    resume = parse_resume(resume_file)

    # 2. Make dataframe and add jobl and resume
    df = pd.DataFrame([
        {'Job Listing': jobl},
        {'Resume': resume}
    ])

    # 2. Load model and make embeddings
    df['Job Embedding'] = embed(jobl).numpy()[0]
    df['Resume Embedding'] = embed(resume).numpy()[0]

    # 3. Get Similarity Score
    df['Similarity Score'] = 1 - spatial.distance.cosine(df['Job Embedding'][0], df['Resume Embedding'][0])

    print(df)

if __name__=='__main__':
    main('files/nova_jl.pdf', 'files/resume.pdf')
