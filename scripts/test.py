import site, sys
import datetime, time
import argparse
import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))


from django.core.management import setup_environ
sys.path.append('/home/ubuntu/code/dg_git')
site.addsitedir('/home/ubuntu/.virtualenv/dg_production/lib/python2.7/site-packages/')

import settings
setup_environ(settings)


from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
from django.core.urlresolvers import reverse
import settings

email_list=['system@digitalgreen.org']
fid=open('/tmp/master_etl.log')
lines=fid.read();
fid.close()
text_content=lines.split("Log")[-1]
subject = 'ETL status for '+str(datetime.date.today())
from_email = 'server@digitalgreen.org'
for email in email_list:
	if email:
                to_email = email
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
                msg.send()
