from global_objects import db


class Product(db.Model):
    __tablename__ = "Product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.REAL, nullable=False)
    tax_code = db.Column(db.Integer, db.ForeignKey("TaxCode.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "tax_code": self.tax_code
        }