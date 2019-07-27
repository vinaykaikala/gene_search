from flask_restplus import reqparse

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('lookup', type=str, required=True,  help='Gene name example: BRAF')
search_arguments.add_argument('species', type=str,  help='species name for gene search example: chlorocebus_sabaeus')
