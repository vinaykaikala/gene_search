#!/bin/bash

#initiate the celery worker and the genequery application
service rabbitmq-server start
celery -A gene_query.app.celery worker --loglevel=info &> /dev/null &
genequery_api -p 80 
