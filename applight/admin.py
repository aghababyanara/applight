from django.contrib import admin

from .models import (
    Header,
    About,
    Video,
    FeaturesMain,
    Features,
    Team,
    Testimonial,
    FAQ,
    Block,
    Contact,
    FormSubmission
)


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Header.objects.exists():
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj = None ):
        return False



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.count()>3:
            return False

        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj = None ):
        return True

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Video.objects.count() >= 1:
            return False

        return super().has_add_permission(request)


    def has_delete_permission(self, request, obj=None):
        return True

class FeaturesModelInline(admin.TabularInline):
    model = Features
    extra = 1

@admin.register(FeaturesMain)
class FeaturesCentralAdmin(admin.ModelAdmin):
    inlines=[FeaturesModelInline]
    def has_add_permission(self,request):
        if FeaturesMain.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display=("full_name","email","subject","created_at")


admin.site.register(FAQ)
admin.site.register(Block)
admin.site.register(Contact)





