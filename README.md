# Django 기본 파일
### 기본 프로젝트 생성 시 파일구조
```c
project 
├── project_name
│  ├── db.sqlite3
│  ├── manage.py
│  ├── settings.py
│  ├── urls.py
│  └── wsgi.py
└── requirements.txt
```
- manage.py : 사이트 관리를 도와주는 역할을 하는 스크립트, 서버구동, model생성 등 내용이 들어 있는 스크립트
- settings.py : 프로젝트의 기본 셋팅 정보가 담겨있음, auth_user, install_app, secret key 등 정보를 기입하고 다른 파일에서 불러와 사용
- urls.py : web url주소를 관리하는 파일이다. project에 urls 에서는 기본적인 url동작이나 앱에서 연결 시켜주는 url 등을 관리한다.
- wsgi.py : wsgi(Web Server Gateway Interface)란 웹서버와 파이썬 웹 애플리케이션 개발 환경 간의 인터페이스에 대한 규칙을 정의한다.
- requirements.txt : 자신이 설치한 라이브러리들을 정리하여 넣을 수 있는 텍스트 파일 
