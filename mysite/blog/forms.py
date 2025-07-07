from django import forms
from blog.models import BlogModel

class BlogForms(forms.ModelForm):
    # Meta 클래스: 클래스 안에 클래스를 설계
    class Meta:
        # 실제로 디비에 전달해서 저장할 내용만
        # fields에 이쓴 ㄴ요소는 html의 form 태그 안에 name속성이 다 있어야 한다.
        model = BlogModel
        fields = ['title', 'contents', 'writer']
        labels = {
            'title': '제목',
            'writer': '작성자',
            'contents': '내용'
        }


