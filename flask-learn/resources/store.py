from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from db import db
from models import StoreModel
from schema import StoresSchema


blp = Blueprint("Stores", "stores", description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoresSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        db.session.delete(store)
        db.session.commit()

        return {"message":"Store deleted successfully"}


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoresSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoresSchema)
    @blp.response(201, StoresSchema)
    def post(self, store_data):
        """
        Converting data types from post method into key-value pairs
        """
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()

        except IntegrityError:  
            abort(
                400,
                message="A store with that name already exists"
            )  

        except SQLAlchemyError:
            abort(
                500,
                message="An error occurred creating item store"
            )

        return store        
        