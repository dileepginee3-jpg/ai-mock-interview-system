from flask import Flask, render_template
from config import Config
from models.database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from controllers.main_controller import main_bp
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run()
