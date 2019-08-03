import logging

from flask import request
from flask_restplus import Resource
from gene_query.api.search.business import get_genes
from gene_query.api.search.serializers import search_result
from gene_query.api.search.parsers import search_arguments
from gene_query.api.restplus import api
from gene_query.database.models import GeneAutoComplete

log = logging.getLogger(__name__)

ns = api.namespace('search/gene', description='Operations to gene search')


@ns.route('/')
@api.response(405, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'Found gene information')
class GeneSearch(Resource):
    @api.expect(search_arguments,validate=True)
    @api.marshal_list_with(search_result)
    def get(self):
        """
        Returns gene search result.
        * Send a JSON object with the new lookup  in the request body.
        ```
        {
          "lookup": "ter",
          "species": "homo_sapiens"
        }
        ```
        """
        args = search_arguments.parse_args()
        lookup, species = args['lookup'], args['species']
        result, error_code = get_genes(lookup, species)
        return result, error_code
