from gene_query.database import db as mysql

class GeneAutoComplete(mysql.Model):
    __tablename__ = 'gene_autocomplete'
    species = mysql.Column(mysql.String(255), nullable=False)
    stable_id = mysql.Column(mysql.String(128), nullable=False , primary_key=True)
    display_label = mysql.Column(mysql.String(128), nullable=False)
    location = mysql.Column(mysql.String(60), nullable=False)
    db = mysql.Column(mysql.String(128), nullable=False)