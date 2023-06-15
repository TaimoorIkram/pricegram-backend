import tensorflow_hub as hub
import numpy as np
from thefuzz import fuzz
from sklearn.metrics.pairwise import cosine_similarity
from api.serializers import ProductSerializer
import nltk
from restbase.models import Product
nltk.download('punkt')

class Initializer():
    def load_embeddings(self):
        with open(self.embeddings_path, 'r') as f:
            embeddings = eval(f.read())
            self.embeddings = np.array(embeddings)

    def load_model(self):
        model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        self.encoder = lambda x: model([x]).numpy()

class Utils(Initializer):
    def preprocess_query(self, query:str):
        query = query.lower().strip()
        return " ".join(query.split())

    def encode_query(self, query:str):
        return self.encoder(query)

    def find_cluster(self, encoder_query, cluster_size):
        similarity_scores = cosine_similarity(encoder_query, self.embeddings)
        return np.argsort(-similarity_scores.flatten())[:cluster_size]

    def extract_ngrams(self, query):
        tokens = query.split()

        result = []
        for i in range(1, len(query)+1):
            result.extend([set(i) for i in nltk.ngrams(tokens, i)])
        return [" ".join(i) for i in result]

    def sort_cluster(self, query:str, best_cluster):
        grams = self.extract_ngrams(query)

        matching_optons = [
            fuzz.partial_ratio,
            fuzz.ratio,
            fuzz.token_sort_ratio,
            fuzz.token_set_ratio,
        ]

        scores = []
        for product in best_cluster:
            processed_product = self.preprocess_query(str(product))
            score = 0
            for gram in grams:
                score += sum([r(processed_product, gram) for r in matching_optons])
            scores.append(
                [product, score]
            )
        products = [i[0] for i in sorted(scores, key=lambda x: x[1], reverse=True)]

        return products

class SearchEngine(Utils):
    def __init__(self, data_fetcher, embeddings_path=None, model_path=None):
        self.embeddings_path = embeddings_path
        self.model_path = model_path
        self.data_fetcher = data_fetcher
        self.load_embeddings()
        self.load_model()

    def search(self, query, n_rec):
        processed_query = self.preprocess_query(query)
        query_embeddings = self.encode_query(processed_query)
        best_cluster_ids = self.find_cluster(query_embeddings, n_rec)
        best_cluster = self.data_fetcher(best_cluster_ids)
        sorted_best_cluster = self.sort_cluster(processed_query, best_cluster)

        return sorted_best_cluster


def data_fetcher(pks):
    ids = pks.tolist()
    products = Product.objects.filter(id__in=ids)
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return(data)
      


engine = SearchEngine(
    data_fetcher = data_fetcher,
    embeddings_path = "D:\\pricegram-backend\\api\\searchmodel\\use_embeddings.txt",
)


