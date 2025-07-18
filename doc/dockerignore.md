# .dockerignore 파일의 역할과 항목 설명

## 1. .dockerignore의 역할
- `docker build` 시 **복사하지 않을 파일/폴더**를 명시
- 이미지 크기 최적화, 빌드 속도 향상, 민감 정보 제외 등 `gitignore`와 유사한 효과 제공

## 2. 각 항목의 이유

### .git
- Git 저장소 자체는 컨테이너 실행과 무관
- 컨테이너는 실행만을 담당함

### .gitignore
- `git`에서 무시할 파일 목록
- 도커 이미지에 필요 없음 

### .dockerignore
- 자신을 다시 복사할 필요 없음

### Dockerfile
- Dockerfile은 **호스트의 이미지 빌드 정의용** 파일
- 컨테이너 내부에서 다시 쓸 일이 없으므로 제외

## ✅ 요약
`.dockerignore`는 `Dockerfile`의 `.gitignore`와 같은 역할을 하며, 불필요한 파일을 제외해 효율적인 이미지를 만들 수 있음
