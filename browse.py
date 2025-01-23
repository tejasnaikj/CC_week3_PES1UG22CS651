from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    return [Product.load(product) for product in dao.list_products()]



def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)

#I have replaced eval with json.loads because eval() can execute arbitrary Python code, potentially running malicious scripts 
#if the input is compromised. json.loads() safely parses JSON strings, preventing code injection risks by strictly interpreting 
#structured data without executing any code, m…


