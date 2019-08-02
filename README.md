gene_search application
=============

- Instal
    --
``` 
    - git clone  https://github.com/vinaykaikala/gene_search.git
    - cd gene_search
    - python setup.py  install
    - pip install -r requirements.txt
    - pip install .
``` 
 - Run application
    --
```
    - genequery_api -p 8090
```
    
 
 - Example:
    --
```
    To use swager UI: http://localhost:8090/api/
    - 1: Search by partial lookup name : brap 
        --
        -    http://localhost:8090/api/search/gene/?lookup=brap
    - 2: Search by partial lookup name and species name
        --
        - http://localhost:8090/api/search/gene/?lookup=brap&species=amphilophus_citrinellus
```
 
 - Run Test Case
    --
```
    - python -m pytest
```

 - Run Docker Container 
    --
```
   - docker run  --network=host -it vinaykaikala/genequery:latest -p 500	
```	

```

- Submit and run background jobs with Rabbitmq, celery
=======

- Install
--------
- sudo apt-get install rabbitmq-server
- pip install celery

- Start rabbitmq message broker, celery worker and flask
-------
- cd gene_search	
- celery -A app.celery worker --loglevel=info
- genequery_api -p 8090 

 - Example:
    --
    To use swager UI: http://localhost:8090/api/
    - 1: submit job to queue
        --
        -  http://localhost:5000/api/rabbitmq/gene/?lookup=tre
	```
		-Return the status and task_id submitted to queue
		----
		-{ "status": "PENDING",  "task_id": "99081de1-2290-420d-96aa-0ca4c7221b22"}
        ``` 
    - 2: Get status and result for submitted job
        --
        - http://localhost:5000/api/rabbitmq/gene/status?qid=99081de1-2290-420d-96aa-0ca4c7221b22
        ```
		{
 		 "status": "SUCCESS",
		  "total_records": 1,
		  "lookup": "tre",
		  "species": null,
		  "data": [
			    {
			      "species": "drosophila_melanogaster",
			      "stable_id": "FBgn0020620",
			      "display_label": "RN-tre",
			      "location": "2R:13984815-13990707",
			      "db": "core"
			    }
			  ]
		}

	```

```

Sample application deployed in heroku
=====
-	URL: https://genequery.herokuapp.com/
