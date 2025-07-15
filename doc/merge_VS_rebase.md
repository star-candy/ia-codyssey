# Merge vs Rebase

기본적으로 Git에서 브랜치를 병합하거나 히스토리를 정리하는 방식은 `merge`와 `rebase`가 존재한다
다만 협업 상황에서는 `merge` 사용이 추천된다

---

## 1. Merge란?

`merge` 각 branch의 분기를 유지한 채 코드 내용만 업데이트 하는 방식
branch 간의 작업 내역은 **그대로 유지**되며, **통합된 새 커밋**(`merge commit`)이 기록된다.

###  특징
- 히스토리를 보존하며 두 작업 흐름을 하나로 합침
- 협업 이력 추적에 용이함
- 충돌 발생 시 명확한 기준을 제공

###  예시

```bash
git checkout main
git merge feature-branch
```

---

## 2. Rebase란?

`Rebase`병합 대상 branch의 내용을 현재 branch 위로 쌓는 방식
 브랜치 간의 작업 내역은 **통합되며**, **병합 커밋은 없음**

###  특징
- 히스토리 유지 없이 한 branch 위로 작업 내용을 쌓는 방식
- 단일 라닝의 깔끔한 로그 구성 가능
- 협업시 높은 충돌 가능성

###  예시

```bash
git checkout feature-branch
git rebase main
```


