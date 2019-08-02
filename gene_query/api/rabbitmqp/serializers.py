from flask_restplus import fields
from gene_query.api.restplus import api

search_result = api.model('Gene result information', {
    'species': fields.String(readOnly=True, description='The Species Gene Belong TO'),
    'stable_id': fields.String(required=True, description='Gene Stable ID'),
    'display_label': fields.String(required=True, description='Gene Name'),
    'location' : fields.String(required=True, description='Gene Location'),
    'db': fields.String(required=True, description='Gene db'),
})

gene_list = api.model('Gene result', {'items': fields.List(fields.Nested(search_result))})


