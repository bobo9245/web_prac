from django import forms
from .models import User


# form 필드 설정
class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, 
        max_length=32, 
        label='이름'
    )

    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        }, 
        widget=forms.EmailInput, 
        max_length=128, 
        label='이메일'
    )

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }, 
        widget=forms.PasswordInput, 
        max_length=64, 
        label='비밀번호'
    )

    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 다시 입력해주세요.'
        }, 
        widget=forms.PasswordInput, 
        max_length=64, 
        label='비밀번호 재입력'
    )

    # 유효성 검사
    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            self.add_error('password', "비밀번호가 같지 않습니다.")
        elif User.objects.filter(email=email):
            self.add_error('email', "이미 존재하는 이메일입니다.")


class LoginForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32,
        label='사용자 이름'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        max_length=64,
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            self.add_error('name', '아이디가 존재하지 않습니다.')
            return

        if password != user.password:
            self.add_error('password', '비밀번호를 틀렸습니다.')
        else:
            self.user_id = user.id