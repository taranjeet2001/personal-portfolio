from django.contrib import admin

from .models import Certification, Experience, PortfolioProfile, ProfileTag, Skill, contact


class ProfileTagInline(admin.TabularInline):
    model = ProfileTag
    extra = 0


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class CertificationInline(admin.StackedInline):
    model = Certification
    extra = 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "headline", "email", "phone")
    inlines = [ProfileTagInline, ExperienceInline, CertificationInline, SkillInline]

    def has_add_permission(self, request):
        return not PortfolioProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]
