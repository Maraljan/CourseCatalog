from django import forms


class CourseForm(forms.Form):
    course_name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    detail_info = forms.CharField(required=True, widget=forms.Textarea)
    start_time = forms.DateField(required=True)
    end_time = forms.DateField(required=True)
    image = forms.ImageField()


class SearchForm(forms.Form):
    query = forms.CharField(required=False)
    start_time = forms.DateField(required=False)
