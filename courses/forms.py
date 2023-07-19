from django import forms
from django.forms import SelectMultiple, TextInput, Textarea

from courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','imageUrl','slug')
        labels = {
            'title': 'Kurs Başlığı',
            'description': 'Açıklama',
            'imageUrl': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
            'imageUrl': TextInput(attrs={"class":"form-control"}),
            'slug': TextInput(attrs={"class":"form-control"})
        }
        error_messages = {
            'title': {
                "required":"Kurs Başlığı Girmelisiniz.",
                "max_length": "Maximum 50 karakter girmelisiniz"
            },
            'description': {
                "required":"Açıklama Girmelisiniz."
            },
            'imageUrl': {
                "required":"Resim olmadan olmaz."
            },
            'slug': {
                "required":"Slugsız birşeye benzemez."
            }
        }
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','imageUrl','slug','categories','isActive')
        labels = {
            'title': 'Kurs Başlığı',
            'description': 'Açıklama',
            'imageUrl': 'Image URL',
            'slug': 'Slug'
        }
        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
            'imageUrl': TextInput(attrs={"class":"form-control"}),
            'slug': TextInput(attrs={"class":"form-control"}),
            'categories': SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            'title': {
                "required":"Kurs Başlığı Girmelisiniz.",
                "max_length": "Maximum 50 karakter girmelisiniz"
            },
            'description': {
                "required":"Açıklama Girmelisiniz."
            },
            'imageUrl': {
                "required":"Resim olmadan olmaz."
            },
            'slug': {
                "required":"Slugsız birşeye benzemez."
            }
        }



# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı",
#         required=True,
#         error_messages={
#             "required":"Kurs Başlığı Girmelisiniz."},
#         widget=forms.TextInput(attrs={"class":"form-control"}))
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={"class":"form-control"}),
#         required=True,
#         error_messages={
#             "required":"Açıklama Girmelisiniz."})
#     imageUrl = forms.CharField(
#         widget=forms.TextInput(attrs={"class":"form-control"}),
#         required=True,
#         error_messages={
#         "required":"Resim olmadan olmaz."})
#     slug = forms.SlugField(
#         widget=forms.TextInput(attrs={"class":"form-control"}),
#         required=True,
#         error_messages={
#             "required":"Slug'sız birşeye benzemez."})