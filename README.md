# popcat
Popcat event for Seoul Maker Festival 2022 & 2023

2022 & 2023 서울 메이커축제 출품작: 팝켓

## 프로젝트 구조
- popcat/polls
  - `views.py` : 사용자가 접속했을 때 HTML 파일 전송
  - `consumers.py` : 실시간 통신 (사실상 핵심 코드)
  - templates/polls
    - `base.html` : 모든 HTML 파일들의 근간. 여기에서 {% block content %} 자리에 각 HTML 파일들의 내용이 삽입되어 사용자에게 전송됨
    - `index.html` : 메인 페이지. 고양이 누르면 *아주 귀여운 소리를 내며* 뻐끔거림.
    - `win.html` : 숫자 당첨되었을 때 뜨는 페이지. 주소 뒤쪽의 `?code=ASDF`로 당첨코드 확인 가능.
  - static/polls
    - css : 각 HTML들에 맞는 CSS 파일 들어가있음
    - js/`count.js` : 메인 페이지에서 클릭되었을 때 점수 올리고, 서버와 실시간 통신하는 모든 코드가 담겨있음

## 개발환경 설정
> 명령어들은 vscode에서 Ctrl+J를 누르면 나오는 터미널 창에 입력하면 됩니다.

### 0. Python, vscode, git 설치
설치 안되어있는 것들만 설치하면 됩니다
* Python (>=3.9): https://www.python.org/downloads/
* Visual Studio Code: https://code.visualstudio.com/
* Git: https://git-scm.com/download/win


### 1. 프로젝트 다운로드 (git clone)
```commandline
git clone https://github.com/jsrodela/life4cuts
cd life4cuts
```

### 2. 필요 프로그램 설치
> Redis: WebSocket(실시간 통신)에 사용되는 프로그램

* [Redis for Windows](https://github.com/tporadowski/redis/releases) .msi 다운로드 후 실행하여 설치

### 3. 가상환경 생성
```commandline
python -m venv .venv
```

아래 명령어로 가상환경에 진입해준다. **이 명령어는 vscode 껐다 킬때마다 쳐야한다.**
```commandline
cmd
cd .venv/scripts
activate.bat
cd ../..
```

### 4. 의존 모듈 설치
```commandline
pip install cryptography==38.0.4
pip install -r requirements.txt
```

### 5. DB 설정
```commandline
python manage.py migrate
```

### 6. settings.json 작성
```json
{
  "production": false,
  "redis": {
    "address": "127.0.0.1",
    "port": 6379
  }
}
```

### 7. 서버 실행

```commandline
python manage.py runserver
```
