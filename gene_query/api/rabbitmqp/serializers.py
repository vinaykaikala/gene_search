from flask_restplus import fields
from gene_query.api.restplus import api

search_result = api.model('GeneAutoComplete', {
    'gene_names': fields.String(required=True, attribute='display_label', description='Gene Name'),
    'location' : fields.String(required=True, description='Gene Location'),
    'Ensembl_stable_ID': fields.String(required=True, attribute='stable_id', description='Gene Stable ID'),
    'species': fields.String(readOnly=True, attribute='species', description='The Species Gene Belong TO'),
    'db': fields.String(description='Gene db'),
},  mask='{gene_names,location,Ensembl_stable_ID,species}')

gene_list = api.model('Gene result',
                      {
                          'status': fields.String(required=True, description='Job Status'),
                          'total_records': fields.Integer(required=True, description='Total Records Found FOr Current Search'),
                          'lookup': fields.String(required=True, description='Gene Name FOr Search'),
                          'species': fields.String(required=True, description='Species name', default="None"),
                          'data': fields.List(fields.Nested(search_result))
                       }
                      )


