#script to upload cocousers, mediators and assigned villages to mediators
from django.core.management.base import BaseCommand
import os
from pandas import *
from geographies.models import *
from programs.models import *
from people.models import *
from coco.models import *
from django.contrib.auth.models import User
import unicodecsv as csv

class Command(BaseCommand):
	def handle(self, *args, **options):
		for filename in os.listdir('/home/ubuntu/django_projects/Mediator'):
		#for filename in os.listdir('C:\Users\Abhishek\Desktop\N'):
			
			error_file = open('/home/ubuntu/django_projects/Mediator/errors.csv', 'wb')
			#error_file = open('C:\Users\Abhishek\Desktop\N\errors.csv', 'wb')
			wrtr = csv.writer(error_file, delimiter=',', quotechar='"')
			wrtr.writerow(["Entry No.", "File Name", "Error"])
		
			#csvfile = open('C:\Users\Abhishek\Desktop\N\\field.csv', 'rb')
			csvfile = open('/home/ubuntu/django_projects/Mediator/field.csv', 'rb')
			rows_file = csv.DictReader(csvfile)

			'''wrtr.writerow(["COCO USER"])	
			i = 0
			for row in rows_file:
				coco_user_set = CocoUser.objects.all()
				coco_map = [entry.user.username for entry in coco_user_set]
				user = User.objects.get(username = unicode(row['Company']))
				try:
					village = Village.objects.get(village_name = unicode(row['Assigned villages']), 
													block__block_name = unicode(row['Taluk']),
													block__district__district_name = unicode(row['District']),
													block__district__state__state_name = unicode(row['State'])
													)
				except Exception as e:
						wrtr.writerow([i, "village not found", e])
						print i,"village not found", e
				partner = Partner.objects.get(partner_name = unicode(row['Company']))

				if unicode(row['Company']) not in coco_map:
					i = i+1
					try:
						cocouser = CocoUser(
								user = user,
								partner = partner
								)
						cocouser.save()
						print i, "coco user done"
						
					except Exception as e:
						wrtr.writerow([i, "coco user error", e])
						print i,"coco user", e

				else : 
					village_set = CocoUser.objects.get(user = user)
					village_map = [entry for entry in village_set.villages.all()]
					if unicode(row['Assigned villages']) not in village_map:
						try:
							cocouser = CocoUser.objects.get(user = user)
							cocouser.villages.add(village)
							cocouser.save()
							print i,  "villages assigned done"
						except Exception as e:
							wrtr.writerow([i, "villages assigned error", e])
							print i, "villages assigned error", e'''

			wrtr.writerow(["Field officers"])	
			i = 0
			for row in rows_file:
				try:
					village = Village.objects.get(village_name = unicode(row['Assigned villages']), 
													block__block_name = unicode(row['Taluk']),
													block__district__district_name = unicode(row['District']),
													block__district__state__state_name = unicode(row['State'])
													)
				except Exception as e:
						wrtr.writerow([i, "village not found", e])
						print i,"village not found", e
				
				partner = Partner.objects.get(partner_name = unicode(row['Company']))

				if (str(row['Phone number']) == ''):
					phone = str('')
				else:
					phone = str(row['Phone number'])

				if (str(row['Training in video production']) == 'No'):
					vp = str('N')
				else:
					vp = str('Y')

				if (str(row['Trained in video screening']) == 'No'):
					vt = str('N')
				else:
					vt = str('Y')

				try:
					animator = Animator(name = unicode(row['Field Officer Name']),
										father_name = unicode(row['Fathers Name']),
										gender = 'M',
										partner = partner,
										phone_no = phone,
										trained_in_video_production = vp,
										trained_in_video_screening = vt)
					animator.save()
				except Exception as e:
						wrtr.writerow([i, "animator", e])
						print i,"animator failed", e

			wrtr.writerow(["Field officer assigned villages"])	
			i = 0
			for row in rows_file:
				animator_set = Animator.objects.filter(partner_id__partner_name = unicode(row['Company'])).all()
				animators = [entry.name for entry in animator_set]

				try:
					village = Village.objects.get(village_name = unicode(row['Assigned villages']), 
													block__block_name = unicode(row['Taluk']),
													block__district__district_name = unicode(row['District']),
													block__district__state__state_name = unicode(row['State'])
													)
				except Exception as e:
						wrtr.writerow([i, "village not found", e])
						print i,"village not found", e

				if unicode(row['Field Officer Name']) in animators:
					try:

						animator = Animator.objects.filter(partner_id__partner_name = unicode(row['Company']), name = unicode(row['Field Officer Name'])).get()
						animator_assigned = AnimatorAssignedVillage(
											animator = animator,
											village = village
											)
						animator_assigned.save()
					except Exception as e:
						wrtr.writerow([i, "animator village assigned", e])
						print i,"animator village failed", e