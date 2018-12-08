#لانشاء نماذج مخصوصة
from django.forms import ModelForm

#جلب الكلاس المراد التعديل عليه
from .models import SignUp

#كلاس التعديل
#وإظهار حقل واحد أو اثنين 
class SignUpForm(ModelForm):
    class Meta:
      model = SignUp
      fields = ['Email','fullName','BirthDate']
      

      #25 Python Web Django Forms and ValidationError
      def clean_Email(self):
          Email=self.cleaned_data.get('Email')
          if not "gmail.com" in Email:
              raise forms.ValidationError("Please Enter Gmail Address")
          return Email
