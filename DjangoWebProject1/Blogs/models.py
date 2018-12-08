from django.db import models

# Create your models here.
class SignUp(models.Model): 
    fullName=models.CharField(max_length=100)
    Email=models.EmailField()
    BirthDate=models.DateField(null=False)
    dateAdd = models.DateField(auto_now=False, auto_now_add=True)
    dateEdit= models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.fullName



