import string
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from core import database as db
import numpy as np

nlp = spacy.load("en_core_web_sm")

abstract_list = db.get_abstract()
# compute the TF-IDF matrix for the corpus
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(abstract_list)
# feature_names = vectorizer.get_feature_names_out()


def preprocessing(doc):
    tok_query = [tok.lemma_.lower().strip() for tok in nlp(str(doc)) if not tok.like_num and not tok.is_punct]
    tok_query = [tok for tok in tok_query if (tok not in nlp.Defaults.stop_words and tok not in string.punctuation and type(tok) != int and type(tok) != float)]
    return ' '.join(tok_query)

def retrieve_docs(query, k):
    processed_query = preprocessing(query)
    # compute the TF-IDF vector for the query
    query_vector = vectorizer.transform([processed_query])

    # compute the cosine similarity between the query vector and the document vectors
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    

    # rank the documents based on the similarity scores
    ranking = np.argsort(similarities)[::-1][:k]
    print('ranking ',ranking)
    # get_abstract_id()

    return {abstract_list[rank]:similarities[rank] for rank in ranking}

