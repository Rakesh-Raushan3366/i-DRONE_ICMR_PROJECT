from django.db import models
from tinymce.models import HTMLField
from django.core.validators import FileExtensionValidator
import re


# Create your models here.

class Carousel(models.Model):
    Title = models.CharField(max_length=255, null=True, blank=True)
    Heading = models.CharField(max_length=255, null=True, blank=True)
    Description = HTMLField(null=True, blank=True)
    Carousel_pics = models.ImageField(upload_to='uploads/%Y/', verbose_name="Background Image")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.Title or f"Carousel {self.id}"


class About_us(models.Model):
    Title = models.CharField(max_length=1000, null=True, blank=True)
    Heading = models.CharField(max_length=1000, null=True, blank=True)
    Description = HTMLField(null=True, blank=True)
    Background_Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Background Image")
    Front_Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Front Image")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About_us"
        verbose_name_plural = "About_Us"

    def __str__(self):
        return self.Title or f"About_us {self.id}"


class Study(models.Model):
    STATUS_CHOICES = (('Ongoing', 'Ongoing'), ('Completed', 'Completed'))

    Title = models.CharField(max_length=1000, blank=True, verbose_name="Title of the study")
    Description = HTMLField(null=True, blank=True, verbose_name="Description of the study")
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True, blank=True,
                              verbose_name="Choose study status")
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Study"
        verbose_name_plural = "Studies"

    def __str__(self):
        return self.Title or f"Study {self.id}"


class Study_Details(models.Model):
    study = models.OneToOneField(Study, default=None, on_delete=models.CASCADE, related_name='details')
    Title = models.CharField(max_length=1000, blank=True, verbose_name="Title of the study")
    Description = HTMLField(null=True, blank=True, verbose_name="Description of the study")
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Study_Details"
        verbose_name_plural = "Study_Details"

    def __str__(self):
        return self.Title or f"StudyDetails for Study {self.study.id}"


class News(models.Model):
    study = models.OneToOneField(Study, default=None, on_delete=models.CASCADE, related_name='news')

    News_Title = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description = HTMLField(null=True, blank=True, verbose_name="News_description")
    # Image = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="Upload Image")
    Pdf = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_02 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_02 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_02 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="2nd image upload")
    Pdf_02 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="2nd Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_03 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_03 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_03 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="3rd image upload")
    Pdf_03 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="3th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_04 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_04 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_04 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="4th image upload")
    Pdf_04 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="4th Upload pdf file",validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_05 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_05 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_05 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="5th image upload")
    Pdf_05 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="5th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_06 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_06 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_06 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="6th image upload")
    Pdf_06 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="6th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_07 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_07 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_07 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="7th image upload")
    Pdf_07 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="7th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_08 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_08 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_08 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="8th image upload")
    Pdf_08 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="8th Upload pdf file",validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_09 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_09 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_09 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="9th image upload")
    Pdf_09 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="9th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_10 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_10 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_10 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="10th image upload")
    Pdf_10 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="10th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_11 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_11 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_11 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="11th image upload")
    Pdf_11 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True,verbose_name="11th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_12 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_12 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_12 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="12th image upload")
    Pdf_12 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="12th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_13 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_13 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_13 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="13th image upload")
    Pdf_13 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="13th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_14 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_14 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_14 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="14th image upload")
    Pdf_14 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="14th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_15 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_15 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_15 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="15th image upload")
    Pdf_15 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="15th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_16 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_16 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_16 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="16th image upload")
    Pdf_16 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True,verbose_name="16th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_17 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_17 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_17 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="17th image upload")
    Pdf_17 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="17th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_18 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_18 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_18 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="18th image upload")
    Pdf_18 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="18th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_19 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_19 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_19 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="19th image upload")
    Pdf_19 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="19th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_20 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_20 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_20 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="20th image upload")
    Pdf_20 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True,  verbose_name="20th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_21 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_21 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_21 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="21th image upload")
    Pdf_21 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="21th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_22 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_22 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_22 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="22th image upload")
    Pdf_22 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="22th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_23 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_23 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_23 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="23th image upload")
    Pdf_23 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="23th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_24 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_24 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_24 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="24th image upload")
    Pdf_24 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="24th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_25 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_25 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_25 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="25th image upload")
    Pdf_25 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="25th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_26 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_26 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_26 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="26th image upload")
    Pdf_26 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="26th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_27 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_27 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_27 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="27th image upload")
    Pdf_27 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="27th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_28 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_28 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_28 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="28th image upload")
    Pdf_28 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="28th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_29 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_29 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_29 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="29th image upload")
    Pdf_29 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="29th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])


    News_Title_30 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_30 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_30 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="30th image upload")
    Pdf_30 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="30th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_31 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_31 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_31 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="31th image upload")
    Pdf_31 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="31th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_32 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_32 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_32 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="32th image upload")
    Pdf_32 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="32th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_33 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_33 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_33 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="33th image upload")
    Pdf_33 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="33th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_34 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_34 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_34 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="34th image upload")
    Pdf_34 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="34th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_35 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_35 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_35 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="35th image upload")
    Pdf_35 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="35th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_36 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_36 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_36 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="36th image upload")
    Pdf_36 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="36th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_37 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_37 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_37 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="37th image upload")
    Pdf_37 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="37th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_38 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_38 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_38 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="38th image upload")
    Pdf_38 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="38th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_39 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_39 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_39 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="39th image upload")
    Pdf_39 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="39th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_40 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_40 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_40 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="40th image upload")
    Pdf_40 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="40th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_41 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_41 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_41 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="41th image upload")
    Pdf_41 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="41th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_42 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_42 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_42 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="42th image upload")
    Pdf_42 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="42th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_43 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_43 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_43 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="43th image upload")
    Pdf_43 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="43th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_44 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_44 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_44 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="44th image upload")
    Pdf_44 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="44th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_45 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_45 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_45 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="45th image upload")
    Pdf_45 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="45th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_46 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_46 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_46 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="46th image upload")
    Pdf_46 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="46th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_47 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_47 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_47 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="47th image upload")
    Pdf_47 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="47th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_48 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_48 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_48 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="48th image upload")
    Pdf_48 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="48th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_49 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_49 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_49 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="49th image upload")
    Pdf_49 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="49th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    News_Title_50 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="News Title")
    News_description_50 = HTMLField(null=True, blank=True, verbose_name="News_description")
    # img_50 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="50th image upload")
    Pdf_50 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="50th Upload pdf file", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "Study_News"

    def __str__(self):
        return self.News_Title or f"News for Study {self.study.id}"


class Videos(models.Model):
    study = models.OneToOneField(Study, default=None, on_delete=models.CASCADE, related_name='videos')
    Inst_Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Institute Short Name")
    Inst_fullname = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Institute Full Name")
    Date = models.DateField(auto_now=True)
    Description = HTMLField(null=True, blank=True, verbose_name="Description for Video")
    video = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="Upload Video")
    video_02 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="2nd Video Upload")
    video_03 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="3rd Video Upload")
    video_04 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="4th Video Upload")
    video_05 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="5th Video Upload")
    video_06 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="6th Video Upload")
    video_07 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="7th Video Upload")
    video_08 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="8th Video Upload")
    video_09 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="9th Video Upload")
    video_10 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="10th Video Upload")
    video_11 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="11th Video Upload")
    video_12 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="12th Video Upload")
    video_13 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="13th Video Upload")
    video_14 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="14th Video Upload")
    video_15 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="15th Video Upload")
    video_16 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="16th Video Upload")
    video_17 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="17th Video Upload")
    video_18 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="18th Video Upload")
    video_19 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="19th Video Upload")
    video_20 = models.FileField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="20th Video Upload")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Videos"
        verbose_name_plural = "Study_Videos"

    def __str__(self):
        return self.Inst_Name or f"Video for Study {self.study.id}"


class Gallery(models.Model):
    study = models.OneToOneField(Study, default=None, on_delete=models.CASCADE, related_name='gallery')

    Heading = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    Image = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="Upload Image")

    Heading_02 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_02 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_02 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="2nd image upload")

    Heading_03 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_03 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_03 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="3rd image upload")

    Heading_04 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_04 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_04 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="4th image upload")

    Heading_05 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_05 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_05 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="5th image upload")

    Heading_06 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_06 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_06 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="6th image upload")

    Heading_07 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_07 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_07 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="7th image upload")

    Heading_08 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_08 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_08 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="8th image upload")

    Heading_09 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_09 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_09 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="9th image upload")

    Heading_10 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_10 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_10 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="10th image upload")

    Heading_11 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_11 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_11 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="11th image upload")


    Heading_12 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_12 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_12 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="12th image upload")

    Heading_13 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_13 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_13 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="13th image upload")

    Heading_14 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_14 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_14 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="14th image upload")

    Heading_15 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_15 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_15 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="15th image upload")

    Heading_16 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_16 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_16 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="16th image upload")

    Heading_17 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_17 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_17 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="17th image upload")

    Heading_18 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_18 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_18 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="18th image upload")

    Heading_19 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_19 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_19 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="19th image upload")

    Heading_20 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_20 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_20 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="20th image upload")

    Heading_21 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_21 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_21 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="21th image upload")

    Heading_22 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_22 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_22 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="22th image upload")

    Heading_23 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_23 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_23 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="23th image upload")

    Heading_24 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_24 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_24 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="24th image upload")

    Heading_25 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_25 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_25 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="25th image upload")

    Heading_26 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_26 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_26 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="26th image upload")

    Heading_27 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_27 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_27 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="27th image upload")

    Heading_28 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_28 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_28 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="28th image upload")

    Heading_29 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_29 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_29 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="29th image upload")

    Heading_30 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_30 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_30 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="30th image upload")

    Heading_31 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_31 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_31 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="31th image upload")

    Heading_32 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_32 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_32 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="32th image upload")


    Heading_33 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_33 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_33 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="33th image upload")

    Heading_34 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_34 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_34 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="34th image upload")

    Heading_35 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_35 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_35 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="35th image upload")

    Heading_36 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_36 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_36 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="36th image upload")

    Heading_37 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_37 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_37 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="37th image upload")

    Heading_38 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_38 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_38 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="38th image upload")

    Heading_39 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_39 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_39 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="39th image upload")

    Heading_40 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_40 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_40 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="40th image upload")

    Heading_41 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_41 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_41 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="41th image upload")

    Heading_42 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_42 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_42 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="42th image upload")

    Heading_43 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_43 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_43 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="43th image upload")

    Heading_44 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_44 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_44 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="44th image upload")

    Heading_45 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_45 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_45 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="45th image upload")

    Heading_46 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_46 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_46 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="46th image upload")

    Heading_47 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_47 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_47 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="47th image upload")

    Heading_48 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_48 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_48 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="48th image upload")

    Heading_49 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_49 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_49 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="49th image upload")

    Heading_50 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Image")
    Paragraph_50 = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Write Image short description")
    img_50 = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="50th image upload")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Study_Gallery"

    def __str__(self):
        return self.Heading or f"Gallery for Study {self.study.id}"


class Team(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Full Name of Team Member")
    Designation = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Designation of Team Member")
    Description = HTMLField(null=True, blank=True, verbose_name="Short Description")
    Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Upload Picture")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

    def __str__(self):
        return self.Name or f"Team {self.id}"


class Idrone_Team(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Full Name of Team Member")
    Designation = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Designation of Team Member")
    Description = HTMLField(null=True, blank=True, verbose_name="Short Description")
    Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Upload Picture")
    Email_link = models.CharField(max_length=255, null=True, blank=True)
    Linkdin_link = models.CharField(max_length=255, null=True, blank=True)

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Idrone_Team"
        verbose_name_plural = "Idrone_Team"

    def __str__(self):
        return self.Name or f"Idrone_Team {self.id}"


class Research_Techanical_Team(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Full Name of Team Member")
    Designation = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Designation of Team Member")
    Description = HTMLField(null=True, blank=True, verbose_name="Short Description")
    Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Upload Picture")
    Email_link = models.CharField(max_length=255, null=True, blank=True)
    Linkdin_link = models.CharField(max_length=255, null=True, blank=True)

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Research_Techanical_Team"
        verbose_name_plural = "Research_Techanical_Team"

    def __str__(self):
        return self.Name or f"Research_Techanical_Team {self.id}"


class Admin_IT_Team(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Full Name of Team Member")
    Designation = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Designation of Team Member")
    Description = HTMLField(null=True, blank=True, verbose_name="Short Description")
    Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Upload Picture")
    Email_link = models.CharField(max_length=255, null=True, blank=True)
    Linkdin_link = models.CharField(max_length=255, null=True, blank=True)

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Admin_IT_Team"
        verbose_name_plural = "Admin_IT_Team"

    def __str__(self):
        return self.Name or f"Admin_IT_Team {self.id}"


class Documents(models.Model):
    Heading = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of Documents")
    Paragraph = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Shot description of Documents")
    Pdf = models.FileField(upload_to='uploads/%Y/', null=True, blank=True,
                           validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "Document"

    def __str__(self):
        return self.Heading or f"Document {self.id}"


class Institute(models.Model):
    study = models.OneToOneField(Study, default=None, on_delete=models.CASCADE, related_name='institute')
    Institute_Name = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Full Name of the Institute")
    Institute_Heading = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Title of the Institute")
    Description = HTMLField(null=True, blank=True, verbose_name="Institute Description")
    Background_Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Background Image")
    Front_Image = models.ImageField(upload_to='uploads/%Y/', verbose_name="Front Image")

    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Institute"
        verbose_name_plural = "Institute"

    def __str__(self):
        return self.Institute_Name or f"Institute {self.id}"


class Twitter(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name")
    designation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Designation")
    description = HTMLField(null=True, blank=True, verbose_name="Institute Description")
    img = models.ImageField(upload_to='uploads/%Y/', null=True, blank=True, verbose_name="Upload Picture")
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name="Link")
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Twitter"
        verbose_name_plural = "Twitter"

    def __str__(self) -> str:
        return self.name or f"Twitter {self.id}"


class Contact_us(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Full Name")
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name="Email Address")
    phone = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Mobile Number")
    message = models.CharField(max_length=255, null=True, blank=True, verbose_name="Message")
    upload_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact_us"
        verbose_name_plural = "Message"

    def __str__(self) -> str:
        return self.name or f"Contact_us {self.id}"
    


class Statistic(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    upload_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name
    
    def numeric_value(self):
        numeric_part = re.sub(r'[^\d]', '', self.value)
        return numeric_part if numeric_part else '0'
