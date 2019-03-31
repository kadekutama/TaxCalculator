from sanic.response import json
from global_objects import app, db
from models.product import Product
from models.tax_code import TaxCode
from libraries.response_formatter import render_template


async def index(request):
    return render_template("index.html")


async def get_all_products(request, mode=None):
    if mode == "select2":
        products = [{"id": product.id, "text": f"{product.name} | {product.price}"} for product in await Product.query.gino.all()]
    else:
        products = [product.to_dict() for product in await Product.query.gino.all()]

    return json({
        "products": products
    })


def calculate_tax(price, tax_code):
    if tax_code == 1:
        return 10.0 * price / 100.0
    elif tax_code == 2:
        return 10.0 + (2.0 * price / 100.0)
    else:
        if price < 100.0:
            return 0.0
        return 1.0 * (price - 100.0) / 100.0

async def get_bill(request):
    if "products" not in request.json or not request.json["products"]:
        return json({"message": "Bad request"}, status=400)

    products = request.json["products"]
    price_subtotal = 0.0
    tax_subtotal = 0.0
    grand_total = 0.0
    detail_bill = []

    for product_id in products:
        if type(product_id) != int:
            return json({"message": "Bad request"}, status=400)

        try:
            product = await Product.get(product_id)
            if not product:
                return json({"message": "Data not found"}, status=404)
            tax_code = await TaxCode.get(product.tax_code)

            tax = calculate_tax(product.price, product.tax_code)
            tax_subtotal += tax
            price_subtotal += product.price
            grand_total += product.price + tax

            cart = {
                "name": product.name,
                "price": product.price,
                "tax_code": product.tax_code,
                "type": tax_code.name,
                "refundable": "Yes" if tax_code.refundable else "No",
                "tax": tax,
                "amount": tax + product.price
            }
            detail_bill.append(cart)
        except:
            return json({"message": "Internal server error"}, status=500)

    return json({
        "detail_bill": detail_bill,
        "price_subtotal": price_subtotal,
        "tax_subtotal": tax_subtotal,
        "grand_total": grand_total
    })