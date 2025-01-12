from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+0000000'. Up to 15 digits allowed."
)

class Header(models.Model):
    title=models.CharField(max_length=50, db_index=True, verbose_name="title")
    subtitle=models.CharField(max_length=150, db_index=True)
    content=models.TextField(max_length=255, db_index=True)
    ios_url=models.URLField(db_index=True)
    app_store=models.ImageField(upload_to="header",  db_index=True)
    android_url=models.URLField(db_index=True)
    google_market=models.ImageField(upload_to="header",  db_index=True)
    header_img=models.ImageField(upload_to="header",  db_index=True)

    def __str__(self):
        return self.title

class Block(models.Model):
    title=models.CharField(max_length=160, db_index=True, verbose_name="title")
    subtitle=models.TextField(max_length=500, db_index=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title=models.CharField(max_length=160, db_index=True, verbose_name="title")
    subtitle=models.TextField(max_length=500, db_index=True)
    icon=models.CharField(max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="About Item"
        verbose_name_plural="About Item"

class Video(models.Model):
    title=models.CharField(max_length=160, db_index=True, verbose_name="title")
    video_url=models.URLField(db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Video"
        verbose_name_plural="Video"

class FeaturesMain(models.Model):
    features_img=models.ImageField(upload_to="features", db_index=True)
    description=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Features Main"

class Features(models.Model):
    main=models.ForeignKey(FeaturesMain, on_delete=models.CASCADE, related_name="items", verbose_name="title")
    title=models.CharField(max_length=255, db_index=True)
    subtitle=models.CharField(max_length=500, db_index=True)
    icon=models.CharField(max_length=255)
    delay=models.CharField(max_length=255)

    def __str__(self):
        return f"Features: {self.title}"

class Team(models.Model):
    team_img=models.ImageField(upload_to="team")
    team_full_name=models.CharField(max_length=255)
    team_position=models.CharField(max_length=255)
    delay=models.CharField(max_length=255)

    def __str__(self):
        return self.team_full_name

class Testimonial(models.Model):
    t_img=models.ImageField(upload_to="testimonials")
    t_full_name=models.CharField(max_length=255)
    t_role=models.CharField(max_length=255)
    t_review=models.TextField(max_length=255)

    def __str__(self):
        return self.t_full_name

class FAQ(models.Model):
    title=models.CharField(max_length=255, db_index=True, verbose_name="title")
    subtitle=models.TextField(max_length=500, db_index=True)
    delay=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Contact(models.Model):
    address=models.CharField(max_length=255)
    phone = models.CharField(max_length=15, validators=[phone_validator])
    email=models.EmailField(max_length=255)
    working_hours=models.CharField(max_length=255)

    def __str__(self):
        return "Contacts"

class FormSubmission(models.Model):
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255, blank=True, null=True)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.full_name}"
