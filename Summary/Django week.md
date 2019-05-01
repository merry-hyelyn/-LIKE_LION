## Model & admin<br><br>

MTV 패턴 : Model, Templates, View<br><br>
    ▲ Model : 데이터 베이스를 다루는 부분<br>
    △ Templates : 사용자의 화면에 보여지는 부분<br>
    △ View : 어떤 때에 사용자가 원하는 화면을 보여줄지 다루는 부분<br><br>

데이터의 형식을 'class'의 형태로 정의 -> models.py 에다가!<br><br>

즉, models.py에 저장된 class의 형태로 여러 개의 데이터(객체) 생성<br><br>

DateBase = 정보 저장 공간<br>
Django 와 별개 -> 여러 개의 데이터 베이스 사용 가능!<br>
settings.py에 새로운 데이터 베이스 등록 후 사용 가능<br><br>

models.py에 저장된 형태 -> 데이터 베이스한테 알려야 한다!(명령어 사용)<br><br>

$ python manage.py makemigrations<br>
models.py에 저장된 데이터의 형태를 알리는 명령어<br>

$ python manage.py migrate<br>
실제로 데이터 베이스에 데이터를 적용하는 명령어<br>

데이터 활용 준비 끝? -> 아니다! admin계정 생성<br><br>

계정 생성 명령어<br>
$ python manage.py createsuperuser<br>
