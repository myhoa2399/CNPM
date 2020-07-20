import json
from saleapp import app
import os
def read_products():
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        return  json.load(f)
        if keyword:
            return [product for product in product["name"].lower().find(keyword.lower()) >= 0]
        if from_price and to_price:
            return [product for product in product if product["price"] >= from_price and product <= to_price]
    return products
def read_products_by_cate_id(cate_id):
    return [product for product in read_products() if product["category_id"] == cate_id]

if __name__ == "__main__":
    print(read_products())
