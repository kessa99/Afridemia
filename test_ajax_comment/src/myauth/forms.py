# from django import forms
# from django.contrib.auth.models import User

# class SignUpForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100,
#         widget=forms.TextInput(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
#     )

#     last_name = forms.CharField(max_length=100,
#         widget=forms.TextInput(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
#     )

#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'password1',
#             'password2',
#         ]

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100,
#         widget=forms.TextInput(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
#     )
#     password = forms.CharField(widget=forms.PasswordInput)

#     # class Meta:
#     #     fields = ['username', 'password']
        
