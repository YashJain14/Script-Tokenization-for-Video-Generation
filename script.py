import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function to tokenize paragraphs into sentences
def tokenize_sentences(paragraph):
    doc = nlp(paragraph)
    sentences = [sent.text for sent in doc.sents]
    return sentences

# Function to tokenize sentences into phrases excluding pronouns
def tokenize_phrases(sentence):
    doc = nlp(sentence)
    phrases = [chunk.text for chunk in doc.noun_chunks if not any(token.pos_ == 'PRON' for token in chunk)]
    return phrases

# Example paragraph
paragraph = """
    The sun was setting behind the tall trees, casting long shadows across the forest floor. 
    Birds chirped merrily as they returned to their nests, preparing for the night ahead. 
    A gentle breeze rustled the leaves, carrying with it the scent of pine and earth. 
    In the distance, a river meandered through the landscape, its waters shimmering in the fading light. 
    The tranquility of the forest was broken by the occasional rustle of small animals moving through the underbrush. 
    As dusk descended, the sky turned into a canvas of vibrant colors, painting the clouds with shades of pink, orange, and purple. 
    Fireflies began to emerge, their soft glow adding to the enchanting atmosphere. 
    It was a scene straight out of a fairy tale, where magic lingered in every corner and time seemed to stand still.
"""

# Tokenize paragraph into sentences
sentences = tokenize_sentences(paragraph)

# Tokenize each sentence into phrases
for sentence in sentences:
    phrases = tokenize_phrases(sentence)
    print("Sentence:", sentence)
    print("Phrases:", phrases)
