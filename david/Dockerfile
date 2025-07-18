# 1. 베이스 이미지 설정
FROM python:3

# 2. 작업 디렉토리 설정
WORKDIR /david

# 3. 로컬 파일 전체 복사
COPY . .

# 4. 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너에서 사용될 포트
EXPOSE 80

# 6. 앱 실행 명령
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]
