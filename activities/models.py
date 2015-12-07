import json, datetime
import calendar
from django.db import models
from django.db.models.signals import pre_delete, post_save

from coco.data_log import delete_log, save_log
from coco.base_models import CocoModel
from geographies.models import Village
from programs.models import Partner
from people.models import Animator, Person, PersonGroup
from videos.models import Video, Topic

class Screening(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    date = models.DateField()
    crop_stage =  models.CharField(max_length=10, null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=200, blank=True)
    village = models.ForeignKey(Village)
    animator = models.ForeignKey(Animator, verbose_name = 'Field Officer')
    farmer_groups_targeted = models.ManyToManyField(PersonGroup, verbose_name = 'Farmer Families')
    videoes_screened = models.ManyToManyField(Video, verbose_name='Videos Screened')
    farmers_attendance = models.ManyToManyField(Person, through='PersonMeetingAttendance', blank='False', null='False')
    partner = models.ForeignKey(Partner, verbose_name='Supply Partner')
    
    class Meta:
        unique_together = ("date", "start_time", "end_time", "animator", "village")

    def __unicode__(self):
        return u'%s' % (self.village.village_name)

    def screening_location(self):
        return u'%s (%s) (%s) (%s)' % (self.village.village_name, self.village.block.block_name, self.village.block.district.district_name, self.village.block.district.state.state_name)

post_save.connect(save_log, sender=Screening)
pre_delete.connect(delete_log, sender=Screening)

class PersonMeetingAttendance(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    screening = models.ForeignKey(Screening)
    person = models.ForeignKey(Person)
    interested = models.BooleanField(db_index=True)
    expressed_question = models.CharField(max_length=500, blank=True)
    expressed_adoption_video = models.ForeignKey(Video, related_name='expressed_adoption_video', null=True, blank=True)

    def __unicode__(self):
        return  u'%s' % (self.id)

class PersonAdoptPractice(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    animator = models.ForeignKey(Animator, verbose_name = 'Field Officer')
    group = models.ForeignKey(PersonGroup, verbose_name='Farmer Family')
    topic = models.ForeignKey(Topic)
    date_of_adoption = models.DateField()
    partner = models.ForeignKey(Partner, verbose_name='Supply Partner')
    
    def __unicode__(self):
        return "%s (%s) " % (self.group.name, self.topic.topic_name)

    class Meta:
        unique_together = ("group", "topic", "date_of_adoption")
post_save.connect(save_log, sender=PersonAdoptPractice)
pre_delete.connect(delete_log, sender=PersonAdoptPractice)
