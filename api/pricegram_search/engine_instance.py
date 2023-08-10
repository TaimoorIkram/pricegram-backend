from api.serializers import ProductSerializer
from restbase.models import Product
from .engine import SearchEngine

def data_fetcher(pks):
    ids = pks.tolist()
    products = Product.objects.filter(id__in=ids)
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return data

engine = SearchEngine(
    data_fetcher = data_fetcher,
    dump_path = "api/searchmodel/data/utils",
)