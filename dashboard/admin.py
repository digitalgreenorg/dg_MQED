import operator

from django import forms
from django.conf import settings
from django.conf.urls import patterns
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.encoding import smart_str
from django.forms import TextInput, Textarea
from coco.base_models import NONNEGOTIABLE_OPTION

from activities.models import PersonMeetingAttendance, Screening, PersonAdoptPractice
from people.models import Animator, AnimatorAssignedVillage, Person, PersonGroup
from dashboard.forms import CocoUserForm
from videos.models import  NonNegotiable

class PersonMeetingAttendanceForm(forms.ModelForm):
    person = forms.ModelChoiceField(Animator.objects.none())
    class Meta:
        model = PersonMeetingAttendance

class FarmerAttendanceInline(admin.TabularInline):
    model = PersonMeetingAttendance
    raw_id_fields = ("person",)
    extra = 20


class ScreeningForm(forms.ModelForm):
    class DynamicChoiceField(forms.ChoiceField):
        def clean(self, value):
            return value

    class DynamicMultipleChoiceField(forms.MultipleChoiceField):
        def clean(self, value):
            return value


    #village  = AjaxForeignKeyField(Village, (('village_name',{}),),default_index=0, select_related= None, widget=FilteredSelect(attrs={'onchange':'temp();'}))
    #village = forms.ModelChoiceField(Village.objects, widget=forms.Select(attrs={'onchange':'filter();'}))
    #animator = DynamicChoiceField(widget=forms.Select(attrs={'disabled': 'true'}))
    farmer_groups_targeted = forms.ModelMultipleChoiceField(PersonGroup.objects, widget=forms.SelectMultiple(attrs={'onchange': 'filter_person();'}))
    #farmer_groups_targeted = DynamicMultipleChoiceField(widget=forms.SelectMultiple(attrs={'onchange':'filter_person();'}))
    #farmer_groups_targeted = forms.ModelMultipleChoiceField(queryset=PersonGroup.objects.none())
    #animator = forms.ModelChoiceField(Animator.objects, widget=forms.Select(attrs={'disabled': 'true'}))
    animator = forms.ModelChoiceField(Animator.objects)
    #screening_grade = forms.ChoiceField(widget=forms.RadioSelect(), choices=SCREENING_GRADE)
    #farmers_groups_targeted = forms.ModelChoiceField(PersonGroup.objects, widget=forms.SelectMultiple(attrs={'onchange':'filter_person();'}))

    class Meta:
        model = Screening

class ScreeningAdmin(admin.ModelAdmin):
    filter_horizontal = ('videoes_screened',)
    list_display = ('id', 'date', 'screening_location')
    search_fields = ['user_created__username', 'id', 'village__village_name', 'partner__partner_name','animator__name', 'videoes_screened__title', 'village__block__block_name', 'village__block__district__district_name','village__block__district__state__state_name']
    raw_id_fields = ('village', 'animator', 'farmer_groups_targeted', 'videoes_screened')
    list_filter = ('date',  'village__block__district__state__state_name',  'partner__partner_name')
   
class NonNegotiablesInline(admin.TabularInline):
    model =  NonNegotiable
    raw_id_fields = ("topic",)
    extra = 5


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields':['title','topic','language','summary','village','production_team','persons_shown','women_featured','approval_date','video_suitable_for','youtubeid', 'partner']}),
                
    ]
    list_display = ('id', 'title')
    search_fields = ['id', 'title', 'partner__partner_name' , 'village__village_name', 'village__block__block_name', 'village__block__district__district_name','village__block__district__state__state_name' ]
    list_filter = ('village__block__district__state__state_name', 'partner__partner_name')
    raw_id_fields = ('village', 'persons_shown')

class AnimatorAssignedVillages(admin.StackedInline):
    model = AnimatorAssignedVillage

class AnimatorAdmin(admin.ModelAdmin):
    fields = ('name','father_name','gender','trained_in_video_production','trained_in_video_screening','phone_no','partner')
    inlines = [AnimatorAssignedVillages]
    list_display = ('name', 'partner')
    search_fields = ['name', 'partner__partner_name']

class PersonGroupInline(admin.TabularInline):
    model = PersonGroup
    extra = 5

class AnimatorInline(admin.TabularInline):
    model = Animator
    extra = 5
    exclude = ('assigned_villages',)

class VillageAdmin(admin.ModelAdmin):
    list_display = ('village_name', 'block')
    search_fields = ['village_name', 'block__block_name', 'block__district__state__state_name']
    inlines = [PersonGroupInline]


class PersonInline(admin.TabularInline):
    model = Person
    extra = 30


class PersonGroupForm(forms.ModelForm):
    class Meta:
        model = PersonGroup

    class Media:
        js = (
                settings.STATIC_URL + "js/filter_village.js",
                #settings.STATIC_URL + "js/jquery-1.3.2.min.js",
                #settings.STATIC_URL + "js/ui/ui.core.js",
                #settings.STATIC_URL + "js/ui/ui.sortable.js",
                #settings.STATIC_URL + "js/dynamic_inlines_with_sort.js",
        )

        #css = {
        #        'all':('/media/css/dynamic_inlines_with_sort.css',)
        #}



class PersonGroupAdmin(admin.ModelAdmin):
    inlines = [PersonInline]
    list_display = ('name','father_name','village')
    search_fields = ['name','village__village_name']
    form = PersonGroupForm


class AnimatorAssignedVillageAdmin(admin.ModelAdmin):
    list_display = ('animator','village')
    search_fields = ['animator__name','village__village_name']


class PersonAdoptPracticeInline(admin.StackedInline):
    model = PersonAdoptPractice
    extra = 3

class PersonAdoptPracticeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': forms.CheckboxSelectMultiple(choices=NONNEGOTIABLE_OPTION)},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    list_display = ('id', 'date_of_adoption', '__unicode__')
    list_filter = ('date_of_adoption','group__village__block__district__state__state_name', 'partner__partner_name')
    search_fields = ['user_created__username', 'id', 'group__name', 'group__village__village_name', 'topic__topic_name', 'group__village__block__block_name','group__village__block__district__district_name','group__village__block__district__state__state_name']
    raw_id_fields = ('group', 'topic')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__')
    search_fields = ['person_name','village__village_name','group__name']
    raw_id_fields = ('village','group')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_name', 'district')
    search_fields = ['block_name', 'district__district_name', 'district__state__state_name']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name', 'state')
    search_fields = ['district_name', 'state__state_name']

class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name',)
    search_fields = ['state_ name', 'country__country_name']

class CocoUserAdmin(admin.ModelAdmin):
    form = CocoUserForm
    list_display = ('user','partner','get_villages')
    search_fields = ['user__username']

class TopicAdmin(admin.ModelAdmin):
    inlines = [NonNegotiablesInline,]
    search_fields = ['topic_name']
    