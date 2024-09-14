from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt

from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<int:item_id>")
class Item(MethodView):

    @jwt_required(fresh=False)
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    @jwt_required(fresh=True)
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)  # Order matters
    def put(self, item_data, item_id):  # Schema params needs to go before route arguments
        item = ItemModel.query.get(item_id)  # Cant 404 because item might not exist
        if item:  # If item exists update it
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:  # else create new item
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()
        return item

    @jwt_required(fresh=True)
    def delete(self, item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}

@blp.route("/item")
class ItemList(MethodView):

    @jwt_required(fresh=False)
    @blp.response(200, ItemSchema(many=True))  # Works for lists
    def get(self):
        return ItemModel.query.all()  # Does not need to transform it into list then

    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)  # Item schema gets the JSON data
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()  # Save to database file (disk), commits all at once for many add
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return item