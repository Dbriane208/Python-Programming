from flask import request
from flask_restful import Resource
from flask_jwt import jwt_required


#create the database
menus = []

class Menu(Resource):
    @jwt_required()
    def get(self,name):
        menu_item = next(filter(lambda menu: menu['name'] == name,menus),None)
        if menu_item is None:
            return {'message': 'menu item {} does not exist.'.format(name)}, 404
        else:
            return {'menu item': menu_item},200
           
        
    def post(self,name):
        if next(filter(lambda food: food['name'] == name,menus),None):
            return {'message': 'menu item {} already exists'.format(name)}
        
        data = request.get_json()
        updMenu = {
            'name': name,
            'type': data['type'],
            'price': data['price']
        }
        menus.append(updMenu)
        return updMenu, 201
   
    def delete(self,name):
        global menus
        menus = list(filter(lambda menu: menu['name'] != name, menus))
        if menus:
            return {'message': 'menu item {} deleted successfully.'.format(name)}, 200
        else:
          return {'message': 'menu item {} does not exist.'.format(name)}, 404

    def put(self,name): 
        data = request.get_json()
        updMenu = next(filter(lambda menu: menu['name'] == name,menus),None)
        if updMenu is None:
            updMenu = {
                'category': name,
                'price': data['price'],
                'name': data['name'],
                'message': data['message']
            }  
            menus.append(updMenu)
        else:
            updMenu.update(data)
        return updMenu, 200
        
class Menus(Resource):
    def get(self):
        return {'menus': menus}, 200        