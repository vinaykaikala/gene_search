from gene_query.database import db
from gene_query.database.models import GeneAutoComplete as gene_table



def get_genes(lookup, species=None):
    "Returns the lookup gene information"
    #test case : gene_list = gene_table.query.filter_by(stable_id='ENSAPOG00000000240').first()

    if len(lookup) < 3:
        return None, 400

    if species:
        return gene_table.query.filter(gene_table.display_label.like(lookup + "%"), gene_table.species == species).all(), 200

    return gene_table.query.filter(gene_table.display_label.like("%" + lookup)).all(), 200
