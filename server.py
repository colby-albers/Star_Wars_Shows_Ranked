from flask_app import app

from flask_app.controllers.user_login_controller import User
from flask_app.controllers import shows

if __name__=="__main__":
    app.run(debug=True, port=8000)