from flask_restplus import fields
from gene_query.api.restplus import api

search_result = api.model('GeneAutoComplete', {
    'gene_names': fields.String(required=True, attribute='display_label', description='Gene Name'),
    'location' : fields.String(required=True, description='Gene Location'),
    'Ensembl_stable_ID': fields.String(required=True, attribute='stable_id', description='Gene Stable ID'),
    'species': fields.String(readOnly=True, attribute='species', description='The Species Gene Belong TO'),
    'db': fields.String(required=True, description='Gene db'),
},  mask='{gene_names,location,Ensembl_stable_ID,species}')

gene_list = api.model('Gene result', {'items': fields.List(fields.Nested(search_result))})


