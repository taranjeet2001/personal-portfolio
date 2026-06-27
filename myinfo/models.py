from django.db import models


class PortfolioProfile(models.Model):
    full_name = models.CharField(max_length=100)
    headline = models.CharField(max_length=160)
    summary = models.TextField()
    location = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    primary_image = models.ImageField(upload_to="portfolio/images/", blank=True, null=True)
    resume_pdf = models.FileField(upload_to="portfolio/resumes/", blank=True, null=True)

    def __str__(self):
        return self.full_name


class ProfileTag(models.Model):
    profile = models.ForeignKey(
        PortfolioProfile,
        related_name="tags",
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=60)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.label


class Experience(models.Model):
    profile = models.ForeignKey(
        PortfolioProfile,
        related_name="experiences",
        on_delete=models.CASCADE,
    )
    period = models.CharField(max_length=60)
    title = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.title} at {self.company}"


class Certification(models.Model):
    profile = models.ForeignKey(
        PortfolioProfile,
        related_name="certifications",
        on_delete=models.CASCADE,
    )
    period = models.CharField(max_length=60)
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=120)
    credential_url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    profile = models.ForeignKey(
        PortfolioProfile,
        related_name="skills",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=60)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
