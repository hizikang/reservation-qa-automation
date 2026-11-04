# 02. Test Strategy

## 테스트 레벨
- UI 테스트: Selenium
- API 테스트: Requests
- 통합 테스트: 사용자 예약부터 관리자 확인까지의 업무 흐름

## 우선순위
1. 정상 예약 흐름
2. 예약 중복 및 입력값 검증
3. 예약 취소 및 상태 변경
4. 관리자 처리 및 데이터 일관성

## 테스트 환경
- SUT: Seatsurfing (버전 기록 예정)
- 실행 환경: Docker Compose (공식 배포 방식 확인 후 구성)
- 자동화: Python / Pytest / Selenium

## 제외 범위(초기)
- 실제 결제 및 외부 결제사 연동
- 운영 서비스에 대한 부하/침투 테스트
