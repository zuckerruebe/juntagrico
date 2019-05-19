from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.conf.urls import url
from django.utils.translation import gettext as _

from juntagrico.entity.jobs import RecuringJob
from juntagrico.dao.jobtypedao import JobTypeDao
from juntagrico.admins.forms.job_copy_form import JobCopyForm
from juntagrico.util.addons import get_job_inlines
from juntagrico.admins.inlines.assignment_inline import AssignmentInline
from juntagrico.util.admin import formfield_for_coordinator, queryset_for_coordinator


class JobAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'type', 'time', 'slots', 'free_slots']
    actions = ['copy_job', 'mass_copy_job']
    search_fields = ['type__name', 'type__activityarea__name', 'time']
    exclude = ['reminder_sent']
    inlines = [AssignmentInline]
    readonly_fields = ['free_slots']

    def __init__(self, *args, **kwargs):
        self.inlines.extend(get_job_inlines())
        super(JobAdmin, self).__init__(*args, **kwargs)

    def mass_copy_job(self, request, queryset):
        if queryset.count() != 1:
            self.message_user(
                request, _('Genau 1 Job auswählen!'), level=messages.ERROR)
            return HttpResponseRedirect('')

        inst, = queryset.all()
        return HttpResponseRedirect('copy_job/%s/' % inst.id)

    mass_copy_job.short_description = _('Job mehrfach kopieren...')

    def copy_job(self, request, queryset):
        for inst in queryset.all():
            newjob = RecuringJob(
                type=inst.type, slots=inst.slots, time=inst.time)
            newjob.save()

    copy_job.short_description = _('Jobs kopieren')

    def get_form(self, request, obj=None, **kwds):
        if 'copy_job' in request.path:
            return JobCopyForm
        return super(JobAdmin, self).get_form(request, obj, **kwds)

    def get_urls(self):
        urls = super(JobAdmin, self).get_urls()
        my_urls = [
            url(r'^copy_job/(?P<jobid>.*?)/$',
                self.admin_site.admin_view(self.copy_job_view))
        ]
        return my_urls + urls

    def copy_job_view(self, request, jobid):
        # HUGE HACK: modify admin properties just for this view
        tmp_readonly = self.readonly_fields
        tmp_inlines = self.inlines
        self.readonly_fields = []
        self.inlines = []
        res = self.change_view(request, jobid, extra_context={
            'title': 'Copy job'})
        self.readonly_fields = tmp_readonly
        self.inlines = tmp_inlines
        return res

    def get_queryset(self, request):
        return queryset_for_coordinator(self, request, 'type__activityarea__coordinator')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs = formfield_for_coordinator(request,
                                           'type',
                                           'juntagrico.is_area_admin',
                                           JobTypeDao.types_by_coordinator)
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)