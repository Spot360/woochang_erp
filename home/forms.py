from django import forms
# Create your tests here.

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.EmailField(required=True)
    contact_content = forms.CharField(required=True,widget=forms.Textarea)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["contact_name"].label = "Your name:"
        self.fields["contact_email"].label = "Your email:"
        self.fields["contact_subject"].label = "Your email:"
        self.fields["contact_content"].label = "What do you want to say?"
