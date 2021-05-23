FROM continuumio/anaconda:4.4.0
COPY Playground.py Requirements.txt  /Model /usr/local/rf_api/
EXPOSE 8000
WORKDIR /usr/local/rf_api
RUN pip install -r Requirements.txt
CMD python Playground.py