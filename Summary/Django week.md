## Model & admin<br>

MTV 패턴 : Model, Templates, View<br>
    ▲ Model : 데이터 베이스를 다루는 부분<br>
    △ Templates : 사용자의 화면에 보여지는 부분<br>
    △ View : 어떤 때에 사용자가 원하는 화면을 보여줄지 다루는 부분<br>

데이터의 형식을 'class'의 형태로 정의 -> models.py

즉, models.py에 저장된 class의 형태로 여러 개의 데이터 생성

DateBase = 정보 저장 공간
Django 와 별개 -> 여러 개의 데이터 베이스 사용 가능!
settings.py에 새로운 데이터 베이스 등록 후 사용 가능

models.py에 저장된 형태 -> 데이터 베이스한테 알려야 한다!(명령어 사용)

$ python manage.py makemigrations
models.py에 저장된 데이터의 형태를 알리는 명령어

$ python manage.py migrate
실제로 데이터 베이스에 데이터를 적용하는 명령어

데이터 활용 준비 끝? -> 아니다! admin계정 생성

계정 생성 명령어
$ python manage.py createsuperuser
