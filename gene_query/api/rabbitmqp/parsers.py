from flask_restplus import reqparse

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('lookup', type=str, required=True,  help='Gene name example: BRAF')
search_arguments.add_argument('species', type=str,  help='species name for gene search example: chlorocebus_sabaeus')

search_status = reqparse.RequestParser()
search_status.add_argument('qid', type=str, required=True,  help='Query ID from celery')

