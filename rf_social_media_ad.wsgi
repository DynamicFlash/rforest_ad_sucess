
import sys
sys.path.insert(0, "/var/www/rf_social_media_ad")
sys.path.insert(0,'/opt/conda/lib/python3.6/site-packages')
sys.path.insert(0, "/opt/conda/bin/")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from rf_social_media_ad import app as application