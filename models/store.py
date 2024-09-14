from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    # Can have Store object associated with each item and backwards
    # Lazy will not prefetch data from database until we tell it to do that (would take some time)
    # Cascade means when deleting store will also delete all items associated with that store (they cant be nullable)

    # SQL Lite allows us to create item when there are no stores, that won't work in postgres

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")