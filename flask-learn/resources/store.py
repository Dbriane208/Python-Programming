from flask.views import MethodView
from flask_smorest import Blueprint

from schema import StoresSchema,ItemSchema


blp = Blueprint("Stores", "stores", description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoresSchema)
    def get(self, store_id):
        raise NotImplementedError("Getting a store is not implemented.")

    def delete(self, store_id):
        raise NotImplementedError("Deleting a store is not implemented.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        raise NotImplementedError("Listing stores is not implemented.")

    @blp.arguments(StoresSchema)
    @blp.response(201, StoresSchema)
    def post(self, store_data):
        raise NotImplementedError("Creating a store is not implemented.")