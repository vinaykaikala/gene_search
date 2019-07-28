gene_query application
=============

- Instal
    --
    - python setup.py install
    - pip install requirements.txt
    - pip install .
 
 - Run application
    --
    - genequery_api -p 8090
    
 
 - Example:
    --
    To use swager UI: http://localhost:8090/api/
    - 1: Search by partial lookup name : brap 
        --
        -    http://localhost:8090/api/search/gene/?lookup=brap
    - 2: Search by partial looup name and species name
        --
        - http://localhost:8090/api/search/gene/?lookup=brap&species=amphilophus_citrinellus
 
 - Run Test Case
    --
    - python -m pytest


Sample application deployed in heroku
=====
-	URL: https://genequery.herokuapp.com/


