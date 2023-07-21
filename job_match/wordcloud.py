import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def create_word_cloud_with_colors(text, color_func, output_file):
    wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=10, color_func=color_func).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

def color_function(word, font_size, position, orientation, random_state, **kwargs):
    if word in job_listing_text and word in resume_text:
        return 'purple'  # Word appears in both
    elif word in job_listing_text:
        return 'blue'  # Word appears in job listing
    elif word in resume_text:
        return 'red'  # Word appears in resume
    else:
        return 'black'  # Word appears in neither
