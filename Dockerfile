FROM continuumio/anaconda:4.4.0
EXPOSE 8000
RUN apt-get install -y apache2 \
    apache2-dev \
    nano \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/rf_social_media_ad_api/
COPY ./rf_social_media_ad.wsgi /var/www/rf_social_media_ad/rf_social_media_ad.wsgi
COPY rf_social_media_ad.py Requirements.txt  /Model /usr/local/rf_social_media_ad_api/
RUN pip install -r Requirements.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server rf_social_media_ad.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND