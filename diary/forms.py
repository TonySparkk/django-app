from django import forms

class PostForm(forms.Form):
    AUTHOR = (
        ('O', 'Gesti'),
        ('E', 'Reduina'),
    )
    author = forms.ChoiceField(choices=AUTHOR,required=True)
    title = forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs=
    {'placeholder':'Enter the title'}))
    content = forms.CharField(required=True, widget=forms.Textarea())
    def clean_data(self):
        self.author = self.cleaned_data['author']
        self.title = self.cleaned_data['title']
        self.content = self.cleaned_data['content']
        