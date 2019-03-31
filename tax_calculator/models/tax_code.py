from global_objects import db


class TaxCode(db.Model):
    __tablename__ = "TaxCode"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    refundable = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "refundable": self.refundable
        }