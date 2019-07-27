import logging.config
import click
from flask import Flask, Blueprint
from gene_query import settings
from gene_query.api.search.endpoints.gene_search import ns as gene_search_namespace
from gene_query.api.restplus import api
from gene_query.database import db

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(gene_search_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

@click.command()
@click.option('-p', '--port', type=int, default=5000)
def main(port):
    initialize_app(app)
    logging.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format('localhost'))
    app.run(debug=settings.FLASK_DEBUG, port=port)


if __name__ == "__main__":
    main()
