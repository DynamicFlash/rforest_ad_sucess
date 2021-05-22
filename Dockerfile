FROM continuumio/anaconda:4.4.0
COPY /Model Playground.py Requirement.txt /usr/local/rf_api 
EXPOSE 8000
WORKDIR /usr/local/rf_api
RUN pip install -r Requirements.txt
CMD python Playground.py