# Reservation Platform QA Automation

Seatsurfing을 테스트 대상으로 활용하는 웹 예약 플랫폼 QA 자동화 프로젝트입니다.

## Project Overview
- **System Under Test (SUT):** [Seatsurfing](https://github.com/seatsurfing/seatsurfing)
- **Purpose:** 사용자 예약부터 관리자 처리까지 주요 업무 흐름을 검증하고, UI/API 테스트 및 결함 분석 결과를 문서화합니다.
- **QA repository:** 본 저장소는 자동화 코드와 QA 산출물을 관리합니다. Seatsurfing 원본 애플리케이션 소스는 별도 저장소에서 관리합니다.

## Scope (planned)
- 사용자 로그인 및 인증
- 예약 가능한 리소스/시간 조회
- 예약 생성 및 취소
- 관리자 예약 확인 및 관리
- 사용자 화면과 관리자 화면 간 상태 일관성
- API 응답 및 주요 예외 상황

> 실제 테스트 범위와 기능명은 Seatsurfing 버전 및 실행 후 확인한 동작을 기준으로 확정합니다.

## Tech Stack
- Python
- Selenium
- Pytest
- Requests
- Docker Compose (SUT 실행 환경)
- GitHub Actions (추후 CI 구성)

## Repository Structure
```text
config/       테스트 설정
environment/  테스트 대상 실행 환경 관련 문서/설정
tests/        UI, API, 통합 테스트
pages/        Page Object
api/          API 클라이언트 및 API 기능
utils/        드라이버, 로그, 증적 수집 유틸리티
test_data/    테스트 데이터
docs/         QA 문서 및 산출물
reports/      로컬 테스트 결과(기본적으로 Git 제외)
```

## Getting Started
1. Python 및 Docker Desktop 설치
2. `environment/README.md`의 안내에 따라 Seatsurfing 실행 환경 확인
3. 가상환경 생성 및 의존성 설치
4. `config/config.yaml`의 테스트 주소 설정
5. Pytest 실행

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest
```

현재 저장소는 초기 골격입니다. Seatsurfing 실행 및 화면/API 확인 후 실제 테스트를 단계적으로 추가합니다.

## Attribution
Seatsurfing is an independently maintained open-source project. See its [official repository](https://github.com/seatsurfing/seatsurfing) and license terms. This QA repository does not claim authorship of the Seatsurfing application.
