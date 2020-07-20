from flask import Flask, render_template

from saleapp import app, dal


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products_list():
    return render_template("products.html", prod=dal.read_products())


@app.route("/prod/<int:category_id>")
def product_list_by_cate(category_id):
    return render_template("products.html", prod=dal.read_products_by_cate_id(cate_id=category_id))


if __name__ == "__main__":
    app.run(debug=True)