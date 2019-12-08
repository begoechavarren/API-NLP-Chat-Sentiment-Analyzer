import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


def sentiment_analyzer(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)


def tokenize(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens_clean = [e for e in tokens if e not in stop_words]
    return tokens_clean


def flatten_text(lst):
    return " ".join(lst)


def create_df(db, collection):
    data = list(db[collection].find())
    df = pd.DataFrame(data, dtype=str)[['idUser', 'text']]
    df = pd.DataFrame(df.groupby("idUser")["text"].apply(list))
    df['text'] = df['text'].apply(flatten_text).apply(tokenize)
    texts = [" ".join(e) for e in list(df['text'])]
    users = list(df.index)
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(texts)
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      index=users)
    return df


def create_similarity_df(df):
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(similarity_matrix, columns=list(
        df.index), index=list(df.index))
    return sim_df


def find_similarity(user, db, collection):
    df = create_df(db, collection)
    sim_df = create_similarity_df(df)
    result = sim_df[user].sort_values(ascending=False)
    return {result.index[1]: result[result.index[1]]}
