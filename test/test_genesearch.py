from gene_query.api.search.endpoints.gene_search import *
import json
def test_gene_result(client):

    "Test Case1: for given both lookup and  species value"
    # Make a tes call to /search/gene
    response = client.get("api/search/gene/?lookup=BRAF&species=chlorocebus_sabaeus")
    # Validate the response
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json == [{
    "species": "chlorocebus_sabaeus",
    "stable_id": "ENSCSAG00000008218",
    "display_label": "BRAF",
    "location": "21:109545491-109690195",
    "db": "core"
    }]

    "Test Case:2 for given lookup value uppercase"
    response = client.get("api/search/gene/?lookup=BRAP")
    # Validate the response
    assert response.status_code == 200
    assert len(response.json) == 181


    "Test Case:3 for given lookup value in lowercase"
    response = client.get("api/search/gene/?lookup=brap")
    # Validate the response
    assert response.status_code == 200
    assert len(response.json) == 181

    "Test Case:4 for given lookup value length less than 3"
    response = client.get("api/search/gene/?lookup=BR")
    # Validate the response
    assert response.status_code == 400

    "Test Case:5 test post method"
    response = client.post("api/search/gene/")
    assert response.status_code == 405

