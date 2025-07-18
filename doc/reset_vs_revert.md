# Git: reset vs revert 차이점 및 협업 시 revert 권장 이유

Git에서 커밋을 되돌리는 대표적인 명령어는 `reset`과 `revert`로 구분됨 
두 명령어는 모두 이전 상태로 되돌리는 역할을 하지만, **작동 방식과 사용 목적이 완전히 다릅니다.**

---

## 1. `git reset`

### 정의:
- **현재 브랜치의 HEAD(포인터)를 이전 커밋으로 되돌림**
- 커밋 자체를 **기록에서 제거**할 수 있음
- 옵션에 따라 작업 디렉토리, 스테이징 영역도 초기화

### 주요 옵션:
- `--soft`: 커밋만 되돌리고, 스테이징 상태는 유지
- `--mixed`(기본): 커밋과 스테이징 되돌림
- `--hard`: 커밋, 스테이징, 작업 디렉토리까지 모두 되돌림

###  위험성:
- **공용 브랜치에서 사용 시 히스토리가 꼬일 수 있음**
- 삭제된 커밋은 복구가 어려울 수 있음

---

## 2. `git revert`

### 정의:
- 선택한 커밋의 **변경 사항을 반대로 적용**하는 **새 커밋을 생성**
- `커밋을 되돌리는 기록을 남기는 커밋으로 이해할 것`
- 기존 커밋 기록은 **그대로 유지**
- Git 기록이 보존되므로 **안전하게 되돌림**

### 특징:
- 작업 내용은 되돌리지만, **기록은 유지**
- 커밋 로그에 `Revert "커밋 메시지"` 형태로 남음

---



## 4. 협업 시 `revert`를 추천하는 이유

1. **기록 보존**  
   - `revert`는 되돌리는 내용을 새 커밋으로 남기므로, 팀원이 어떤 작업이 취소되었는지 확인할 수 있음

2. **히스토리 충돌 방지**  
   - `reset`은 과거 커밋을 삭제하여 **히스토리 재작성(rewrite)**이 일어나므로  
     협업 중인 다른 사람의 로컬 저장소와 충돌 발생 가능

3. **공용 브랜치에서도 안전하게 사용 가능**  
   - Git 공식 문서에서도 `reset`은 **로컬 브랜치 전용**,  
     `revert`는 **협업 시 기본 되돌리기 방식**으로 권장

---


