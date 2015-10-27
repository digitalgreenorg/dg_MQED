from django.db import models
from django.db.models.signals import pre_delete, post_save

from coco.data_log import delete_log, save_log
from coco.base_models import CocoModel, DAY_CHOICES, GENDER_CHOICES, RELATION_CHOICES, VILLAGE_GROUPS, YesNo_CHOICES
from geographies.models import District, Village
from programs.models import Partner

class Animator(CocoModel):
    id = models.AutoField(primary_key = True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    partner = models.ForeignKey(Partner, verbose_name='company')
    phone_no = models.CharField(max_length=100, blank=True)
    district = models.ForeignKey(District)
    assigned_villages = models.ManyToManyField(Village, related_name='assigned_villages', through='AnimatorAssignedVillage', null=True, blank=True)
    trained_in_video_production = models.CharField(max_length=1, choices=YesNo_CHOICES)
    trained_in_video_screening = models.CharField(max_length=1, choices=YesNo_CHOICES)
    total_adoptions = models.PositiveIntegerField(default=0, blank=True, editable=False) 

    class Meta:
        verbose_name = "Fieled Officer"
        unique_together = ("name", "gender", "partner", "district")

    def get_village(self):
        return None

    def get_partner(self):
        return self.partner.id

    def __unicode__(self):
        return  u'%s (%s)' % (self.name, self.district)

post_save.connect(save_log, sender=Animator)
pre_delete.connect(delete_log, sender=Animator)


class AnimatorAssignedVillage(CocoModel):
    id = models.AutoField(primary_key=True)
    animator = models.ForeignKey(Animator)
    village_group = models.CharField(max_length=100, choices=VILLAGE_GROUPS)
    village = models.ForeignKey(Village)
    start_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Fieled officer assigned village"
        
class PersonGroup(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    aadhar_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    village = models.ForeignKey(Village)
    partner = models.ForeignKey(Partner, verbose_name='company')

    class Meta:
        verbose_name = "Farmer Family"
        verbose_name_plural = 'Farmer Families'
        unique_together = ("name", "father_name", "village")

    def __unicode__(self):
        return  u'%s (%s) (%s)' % (self.name, self.father_name, self.village)
post_save.connect(save_log, sender=PersonGroup)
pre_delete.connect(delete_log, sender=PersonGroup)

class Person(CocoModel):
    id = models.AutoField(primary_key=True)
    old_coco_id = models.BigIntegerField(editable=False, null=True)
    person_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    village = models.ForeignKey(Village)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(max_length=3, null=True, blank=True)
    group = models.ForeignKey(PersonGroup, null=True, blank=True, verbose_name = 'Farmer Family')
    relation_farmer_family = models.CharField(max_length=100, choices=RELATION_CHOICES, null=True, blank=True)
    other_profession = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=10, blank=True)
    partner = models.ForeignKey(Partner, verbose_name='company')
    objects = models.Manager() #The default manager
    
    class Meta:
        unique_together = ("person_name", "father_name", "village")

    def __unicode__(self):
        display = "%s" % (self.person_name)
        display += " (%s)" % self.father_name if self.father_name.strip()!="" else "" 
        display += " (%s)" % self.group.name if self.group is not None else ""
        display += " (%s)" % self.village.village_name
        return  display
post_save.connect(save_log, sender=Person)
pre_delete.connect(delete_log, sender=Person)
