# Django 기본 파일
### 기본 프로젝트 생성 시 파일구조
```
project 
├── project_name
│  ├── __init__.py
│  ├── settings.py
│  ├── urls.py
│  ├── asgi.py
│  └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
```
- manage.py : 사이트 관리를 도와주는 역할을 하는 스크립트, 서버구동, model생성 등 내용이 들어 있는 스크립트
- settings.py : 프로젝트의 기본 셋팅 정보가 담겨있음, auth_user, install_app, secret key 등 정보를 기입하고 다른 파일에서 불러와 사용
- urls.py : web url주소를 관리하는 파일이다. project에 urls 에서는 기본적인 url동작이나 앱에서 연결 시켜주는 url 등을 관리한다.
- wsgi.py : wsgi(Web Server Gateway Interface)란 웹서버와 파이썬 웹 애플리케이션 개발 환경 간의 인터페이스에 대한 규칙을 정의한다.
- requirements.txt : 자신이 설치한 라이브러리들을 정리하여 넣을 수 있는 텍스트 파일 

### DRF(Django Rest Framework)
- Django에서 Restful API를 구현하기 위해 사용되는 서드파티 라이브러리다.
- router, serializer, viewset을 이용하여 Restful API를 구현하는데 앞에 3가지는 꼭 알아 두자
- Serializer
  + [Serializer](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/serializer) 자주 사용하는 JSON파일로 직렬화하는 법
  + [Validation](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/validation) Serializer에서 데이터 검증하는 방법들
  + [ModelSerializer활용법](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/ModelSerializer%EA%B5%AC%ED%98%84)
- [APIView 내용 정리](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/APIView)
- [generics APIView 내용 정리](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/generic%20APIView)
- [ViewSet 내용 정리](https://github.com/hyunseokjoo/prac_django_with_drf/tree/main/info/ViewSet)
