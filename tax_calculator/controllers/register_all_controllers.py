from .products import *


def register_routes(app):
    app.add_route(index, "/", methods=["GET"])
    app.add_route(get_all_products, "/get_all_products/<mode>", methods=["GET"])
    app.add_route(get_bill, "/get_bill", methods=["POST"])