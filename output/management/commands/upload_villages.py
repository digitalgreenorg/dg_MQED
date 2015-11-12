from django.core.management.base import BaseCommand
import os
import unicodecsv as csv
from pandas import *
from geographies.models import *
from programs.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):

		for filename in os.listdir('/home/ubuntu/django_projects/dg_MQED/New'):
			
			error_file = open('/home/ubuntu/django_projects/dg_MQED/errors.csv', 'wb')
			wrtr = csv.writer(error_file, delimiter=',', quotechar='"')
			wrtr.writerow(["Entry No.", "File Name", "Error"])

			#csvfile = open(filename, 'rb')
			#rows_file = csv.DictReader(csvfile)

			xls = ExcelFile('/home/ubuntu/django_projects/dg_MQED/new/'+filename)
			rows_file = xls.parse(xls.sheet_names[0])
			#print df.to_dict()
			
			wrtr.writerow(["Companies"])
			i = 0
			for index, row in rows_file.iterrows():
				partner_querry_set = Partner.objects.values_list('partner_name','id')
				partner_map = dict(partner_querry_set)

				if unicode(row['Company']) not in partner_map:
					i = i+1
					try:
						partner = Partner(user_created_id=1,
									partner_name = unicode(row['Company'])
									)
						partner.save()

					except Exception as e:
						wrtr.writerow([i, filename, e])
						print i, filename, e


			wrtr.writerow(["States"])	
			i = 0
			for index, row in rows_file.iterrows():
				state_querry_set = State.objects.values_list('state_name','id')
				state_map = dict(state_querry_set)
			
				if unicode(row['State']) not in state_map:
					i = i+1
					try:
						state = State(user_created_id=1,
									country_id = 1,
									state_name = unicode(row['State'])
									)
						state.save()

					except Exception as e:
						wrtr.writerow([i, filename, e])
						print i, filename, e
						
			wrtr.writerow(["Districts"])
			i = 0
			for index, row in rows_file.iterrows():
				state_name = State.objects.get(state_name=unicode(row['State']))
				district_querry_set = District.objects.values_list('district_name','id').filter(state_id = state_name.id)
				district_map = dict(district_querry_set)
				if unicode(row['District']) not in district_map:
					i = i+1
					try:
						district = District(user_created_id=1,
									state_id = state_name.id,
									district_name = unicode(row['District'])
									)
						district.save()

					except Exception as e:
						wrtr.writerow([i, filename, e])
						print i, filename, e
						
			wrtr.writerow(["Taluks"])
			i = 0
			for index, row in rows_file.iterrows():
				district_name = District.objects.get(district_name=unicode(row['District']))
				block_querry_set = Block.objects.values_list('block_name','id').filter(district_id = district_name.id)
				block_map = dict(block_querry_set)
				if unicode(row['Taluk']) not in block_map:
					i = i+1
					try:
						block = Block(user_created_id=1,
									district_id = district_name.id,
									block_name = unicode(row['Taluk'])
									)
						block.save()

					except Exception as e:
						wrtr.writerow([i, filename, e])
						print i, filename, e
						

			wrtr.writerow(["Villages"])
			i = 0
			for index, row in rows_file.iterrows():
				block_name = Block.objects.get(block_name=unicode(row['Taluk']))
				village_querry_set = Village.objects.values_list('village_name','id').filter(block_id = block_name.id)
				village_map = dict(village_querry_set)
				if unicode(row['Village']) not in village_map:
					i = i+1
					try:

						village_group = int(row['Control/Treatment (Treatment = 1)'])
						if village_group == 1:
							group = str('Test Group')
						else:
							group = str('Control Group')
						
						village = Village(user_created_id=1,
									block_id = block_name.id,
									village_name = unicode(row['Village']),
									village_group = group 
									)
						village.save()

					except Exception as e:
						wrtr.writerow([i, filename, e])
						print i, filename, e

			error_file.flush()
			error_file.close()
				