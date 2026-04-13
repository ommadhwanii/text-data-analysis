import re
from collections import Counter

def analyze_text(text):
    # Clean text (remove punctuation & convert to lowercase)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Split into words
    words = cleaned_text.split()
    
    # Count word frequency
    word_count = Counter(words)
    
    # Display top 5 words
    print("Top 5 most frequent words:\n")
    for word, count in word_count.most_common(5):
        print(f"{word}: {count}")

# Sample text (you can change this)
text_data = """
AI is amazing. AI is powerful! Data annotation helps train AI models.
"""

analyze_text(text_data)