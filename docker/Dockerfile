FROM continuumio/miniconda3
#Maintainer : Kaikala vinay
#Date : 26-07-2019
#Gene Query 
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN apt-get update -y
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion python-pip python-dev build-essential

RUN apt-get install rabbitmq-server -y
RUN git clone https://github.com/vinaykaikala/gene_search.git
COPY ./docker/base.yml /base.yml
RUN conda env update -f /base.yml

WORKDIR /gene_search
COPY ./docker/genequery_init.sh .
RUN chmod +x genequery_init.sh
ENTRYPOINT ["./genequery_init.sh"]
CMD [""]	
