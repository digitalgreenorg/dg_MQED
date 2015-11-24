from django.contrib.auth.models import User
from django.db import models


# Variables
DAY_CHOICES = (
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday'),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

VIDEO_TYPE = (
        (1, 'Demonstration'),
        (2, 'Success story/ Testimonial'),
        (3, 'Activity Introduction'),
        (4, 'Discussion'),
        (5, 'General Awareness'),
)

STORYBASE = (
        (1, 'Agricultural'),
        (2, 'Institutional'),
        (3, 'Health'),
)

ACTORS = (
        ('I', 'Individual'),
        ('F', 'Family'),
        ('G', 'Group'),
)

VIDEO_STATUS = (
        ('Dissemination', 'Dissemination'),
        ('Dissemination-Training', 'Dissemination-Training'),
        ('Video Production Training', 'Video Production Training'),
)

RELATION_CHOICES = (
    ('Family Member','Family Member'),
    ('Hired Labourer','Hired Labourer'),
    ('Other','Other'),
)

VILLAGE_GROUPS = (
    ('Test Group', 'Test Group'),
    ('Control Group', 'Control Group')
)

YesNo_CHOICES = (
    ('N','No'),
    ('Y','Yes'),
)

WOMEN_FEATURED = (
    ('Farming','Farming'),
    ('Teaching','Teaching'),
    ('Making Decisions','Making Decisions'),
    ('Being Interviwed','Being Interviwed'),
    ('Other Activities','Other Activities'),
    ('Does not feature women','Does not feature women'),
)


class CocoModel(models.Model):
    user_created = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_created", editable = False, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_related_modified",editable = False, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

    def get_village(self):
        return self.village.id
    def get_partner(self):
        return self.village.block.district.partner.id