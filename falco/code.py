from flask import Flask, request
from user import User
from flask_restful import Resource, Api, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
        JWTManager,
        create_access_token,
        create_refresh_token,
        get_jwt_identity,
        jwt_required
        )

app = Flask(__name__)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS']

app.secret_key = os.getenv('SECRET') #secret key

jwt = JWTManager(app)
access_token = ''

class Data(Resource):

     
    def get(self, item):
        return {"items are "+items )}

    def prepare_data(data):
        final_data = key + data
        return haslib.sha256(final_data.encode('utf-8')).hexdigest()) # sent the return value back as the response.

    @jwt_required()
    def post(self, item):
        temp =  random.random()
        information = prepare_data(temp + item)
        token = access_token
        return_data(token, information)


    def return_data(access_token, key):
        result = access_token.split(".", 2)
        if (value == result[1]["name"]):
            return data
        print("try again")

class Login(Resource):

    def post(self):                                 #token generation
        user_parser = reqparse.RequestParser()
        user_parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
        user_parser.add_argument('password', type=str, required=True, help="This field cannot be blank")

        data = user_parser.parse_args()
        user = user_name.get(data['username'], None)
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            
            return{
                    'access_token': access_token,

                    
                    }, 200
        return {"message", "Wrong credentials"}, 401


api.add_resource(Data, '/data/<string:item>')
api.add_resource(Login, '/login')


app.run(debug=True, port = 5002)

