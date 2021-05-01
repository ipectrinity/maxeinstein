from django.contrib.auth.forms import UserCreationForm

class EmailUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)