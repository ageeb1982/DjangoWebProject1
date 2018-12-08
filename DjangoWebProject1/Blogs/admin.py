from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Blogs.form import SignUpForm

# Register your models here.
from .models import SignUp

#لاظهار التفاصيل المخفية
class SignUpAdmin(ModelAdmin):
    list_display=["__str__","Email","BirthDate","dateAdd","dateEdit"]
    form=SignUpForm #نموذج العرض 
    #module=SignUp
    #class Meta:
    #      #form=SignUpForm #نموذج العرض 
    #      #module=SignUp 
    #      pass
        



admin.site.register(SignUp,SignUpAdmin)