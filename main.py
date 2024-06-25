from tests.test_get_most_profitable_products import test_get_most_profitable_products
from db.connection import get_session
with get_session() as session:
    test_get_most_profitable_products(session)