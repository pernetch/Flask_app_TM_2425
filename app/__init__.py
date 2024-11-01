import os
from flask import Flask
from flask_bootstrap import Bootstrap5

from app.utils import *

from app.email.email import send_email

# Importation des blueprints de l'application
# Chaque blueprint contient des routes pour l'application
from app.views.home import home_bp
from app.views.auth import auth_bp
from app.views.user import user_bp

# Fonction automatiquement appelée par le framework Flask lors de l'exécution de la commande python -m flask run permettant de lancer le projet
# La fonction retourne une instance de l'application créée
def create_app():

    # Crée l'application Flask
    app = Flask(__name__)

    # If you want to use Bootstrap 5, import and instanzlize the Bootstrap5 class instead:
    bootstrap = Bootstrap5(app)

    # Chargement des variables de configuration stockées dans le fichier config.py
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), "config.py"))

    # Enreigstrement des blueprints de l'application.
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    #send_email("christian.pernet@websud.ch", "test", "coucou")

    # On retourne l'instance de l'application Flask
    return app