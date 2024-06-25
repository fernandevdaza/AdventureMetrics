from tests.test_get_best_selling_products import test_get_best_selling_products
from db.connection import get_session
with get_session() as session:
    test_get_best_selling_products(session)
