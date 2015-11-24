from django.db import models
from django.db.models.signals import pre_delete, post_save

from coco.data_log import delete_log, save_log
from coco.base_models import ACTORS, CocoModel, VIDEO_STATUS, WOMEN_FEATURED
from geographies.models import Village
from programs.models import Partner
from people.models import Animator, Person

class Topic(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    topic_name = models.CharField(max_length=100, default="None")

    def get_village(self):
        return None

    def get_partner(self):
        return None
    
    def __unicode__(self):
        return self.topic_name

post_save.connect(save_log, sender=Topic)
pre_delete.connect(delete_log, sender=Topic)

class Language(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    language_name = models.CharField(max_length=100, unique='True')

    def get_village(self):
        return None

    def get_partner(self):
        return None
    
    def __unicode__(self):
        return self.language_name
post_save.connect(save_log, sender=Language)
pre_delete.connect(delete_log, sender=Language)


class Video(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='topic')
    duration = models.TimeField(null=True, blank=True)
    language = models.ForeignKey(Language)
    summary = models.TextField(blank=True)
    village = models.ForeignKey(Village)
    production_team = models.ManyToManyField(Animator, related_name='production_team')
    persons_shown = models.ManyToManyField(Person, null=True, blank=True, related_name='persons_shown')
    women_featured = models.CharField(max_length=100, choices=WOMEN_FEATURED)
    approval_date = models.DateField(null=True, blank=True)
    video_suitable_for = models.CharField(max_length=100, choices=VIDEO_STATUS)
    youtubeid = models.CharField(max_length=20, blank=True)
    partner = models.ForeignKey(Partner, verbose_name='Supply Partner')
    
    class Meta:
        unique_together = ("title", "topic", "village")

    def __unicode__(self):
        return  u'%s (%s)' % (self.title, self.village)

    def location(self):
        return u'%s (%s) (%s) (%s)' % (self.village.village_name, self.village.block.block_name, self.village.block.district.district_name, self.village.block.district.state.state_name)

post_save.connect(save_log, sender=Video)
pre_delete.connect(delete_log, sender=Video)

class NonNegotiable(CocoModel):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic)
    non_negotiable = models.CharField(max_length=500)
    chapter =  models.CharField(max_length=500)
    timing =  models.CharField(max_length=500)
    physically_verifiable = models.BooleanField(db_index=True, default=False)
    

    def __unicode__(self):
        return  u'%s' % self.non_negotiable
post_save.connect(save_log, sender=NonNegotiable)
pre_delete.connect(delete_log, sender=NonNegotiable)
