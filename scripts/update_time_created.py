from django.core.management import setup_environ
import dg.settings
setup_environ(dg.settings)

from activities.models import PersonMeetingAttendance, PersonAdoptPractice, Screening
from dashboard.models import Person as OldPerson, PersonAdoptPractice as OldAdoption, PersonMeetingAttendance as OldAttendance,  Screening as OldScreening
from people.models import Person

for person in Person.objects.exclude(old_coco_id__isnull=True):
    old_person = OldPerson.objects.get(id=person.old_coco_id)
    person.time_created = old_person.time_created
    person.save()

print "Person Updated"

