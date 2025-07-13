from flask import Flask #flask 프레임워크에서 Flask 클래스 가져옴

app = Flask(__name__) # Flask 객체 생성, __name__은 현재 모듈의 이름 의미
#모듈의 이름을 Flask에 전달하여 Flask가 해당 모듈을 인식할 수 있도록 함

@app.route("/") # 루트 URL에 대한 라우트 데코레이션
# 루트 접근시 하단 함수 호출
def hello_world():
    return "Hello, DevOps!" # 반환 값이 전달 및 출력됨

if __name__ == "__main__": # import시 실행 방지
    app.run(host="0.0.0.0", port=5000) #host 0.0.0.0 = 모든 IP에서 해당 서버 접근 가능