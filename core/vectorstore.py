from sklearn.feature_extraction.text import TfidfVectorizer

documents = []
vectorizer = TfidfVectorizer()
vectors = None

def create_vectorstore():
    global documents, vectors

    with open("data/sample.txt", "r") as file:
        text = file.read()

    documents = text.split("\n")
    vectors = vectorizer.fit_transform(documents)


def search_vectorstore(query):
    query_vec = vectorizer.transform([query])
    similarity = (vectors * query_vec.T).toarray()

    best_idx = similarity.argmax()
    return documents[best_idx]
