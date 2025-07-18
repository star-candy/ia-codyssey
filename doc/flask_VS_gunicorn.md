# Flask와 Gunicorn의 차이 및 배포 시 Gunicorn 사용 이유

## 1. Flask
- Flask는 마이크로 웹 프레임워크이며 자체 내장 서버를 제공
- `app.run()`으로 개발 중 실행 가능하지만, **개발용** 서버로써 성능/보안/멀티프로세스에 한계

## 2. Gunicorn
- **WSGI(Web Server Gateway Interface)** 기반의 Python 애플리케이션 서버
- **프로덕션 환경에 최적화**, 멀티워크/스레드 기반 동시성 처리 가능
- 성능과 안정성이 뛰어나 Flask, Django와 함께 자주 사용됨

## 3. 배포 시 Gunicorn을 쓰는 이유
- Flask 내장 서버는 단일 프로세스/스레드로 느리고 불안정함
- Gunicorn은 병렬 처리, 예외 복구, 성능 최적화 기능 제공
- **생산 환경에서는 Flask를 Gunicorn으로 감싸서 실행**하는 것이 베스트 프랙티스
