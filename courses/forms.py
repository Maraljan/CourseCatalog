from django import forms


class CourseForm(forms.Form):
    course_name = forms.CharField(required=True)
    # price = forms.FloatField(required=True)
    # detail_info = forms.TextInput()
    # start_time = forms.DateTimeField()
    # end_time = forms.DateTimeField()
