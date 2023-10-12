from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(),
        required=True,
    )
    username = forms.CharField(
        label="사용자 이름",
        required=True,
        help_text="150자 이하 문자, 숫자 그리고 @/./*/-/_ 만 가능합니다.",
    )
    last_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(),
        required=True,
    )
    first_name = forms.CharField(
        label="성",
        widget=forms.TextInput(),
        required=True,
    )
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='''
        <li>다른 개인 정보와 유사한 비밀번호는 사용할 수 없습니다.</li>
        <li>비밀번호는 최소 8자 이상이어야 합니다.</li>
        <li>통상적으로 자주 사용되는 비밀번호는 사용할 수 없습니다.</li>
        <li>숫자로만 이루어진 비밀번호는 사용할 수 없습니다.</li>
        ''',
        required=True,
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text = "확인을 위해 이전과 동일한 비밀번호를 입력하세요.",
        required=True,
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'last_name', 'first_name')
    

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
    
    password = None

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta(PasswordChangeForm):
        model = get_user_model()
    old_password = forms.CharField(
        label="기존 비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password1 = forms.CharField(
        label="새 비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='''
        <li>다른 개인 정보와 유사한 비밀번호는 사용할 수 없습니다.</li>
        <li>비밀번호는 최소 8자 이상이어야 합니다.</li>
        <li>통상적으로 자주 사용되는 비밀번호는 사용할 수 없습니다.</li>
        <li>숫자로만 이루어진 비밀번호는 사용할 수 없습니다.</li>
        ''',
        required=True,
    )
    new_password2 = forms.CharField(
        label="새 비밀번호 확인",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text = "확인을 위해 이전과 동일한 비밀번호를 입력하세요.",
        required=True,
    )