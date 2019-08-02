import logging
from flask import current_app as app
from flask_restplus import Resource
from gene_query.api.rabbitmqp.business import get_genes
from gene_query.api.rabbitmqp.serializers import search_result
from gene_query.api.rabbitmqp.parsers import search_arguments, search_status
from gene_query.api.restplus import api
from gene_query import factory
from celery.result import AsyncResult
from flask import jsonify

celery = factory.celery
log = logging.getLogger(__name__)

ns = api.namespace('rabbitmq/gene', description='operation gene search with rabbitmqp')

@ns.route('/')
@api.response(404, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'Found gene information')
class GeneSearch(Resource):
    @api.expect(search_arguments,validate=True)
    def get(self):
        """
        submit the gene search to rabbitmq message broker
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
        if len(lookup) < 3:
            return None, 400

        result = self.genesearch.delay(lookup, species)
        #result.wait()
        return {'status': result.state, 'task_id': result.id }, 200

    @staticmethod
    @celery.task(bind=True)
    def genesearch(self, lookup, species):
        print('Getting gene result')
        self.update_state(state='PROGRESS',
                          meta={'status': 'Fetching the gene Results'})
        result, status = get_genes(lookup, species)
        complete_result = []
        for each_row in result:
            complete_result.append({
                'species': each_row.species,
                'stable_id': each_row.stable_id,
                'display_label': each_row.display_label,
                'location': each_row.location,
                'db': each_row.db
                    })        

            results = {'status': 'Completed', 'total_records': len(complete_result), 'lookup': lookup, 'species': species, 'data': complete_result} 
        return results

@ns.route('/status')
@api.response(404, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'Found gene information')
class GeneStatus(Resource):
    @api.expect(search_status, validate=True)
#    @api.marshal_list_with(search_result)
    def get(self):

        """
         Get the result from celery by submitting  task id
        """
        args = search_status.parse_args()
        queue_id = args['qid']
        res = GeneSearch.genesearch.AsyncResult(queue_id)
        result = {
                   'status' : res.state,
                   'total_records': res.info.get('total_records', 0),
                   'lookup': res.info.get('lookup', None),
                   'species': res.info.get('species', None),
                   'data': res.info.get('data', None), 
                }
        return result, 200

