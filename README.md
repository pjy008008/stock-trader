# Stock Trader

**Google ADK(Agent Development Kit)** 와 **Gemini 2.5** 모델을 기반으로 구축된 **협업형 멀티 에이전트 주식 투자 분석 시스템**입니다.

이 프로젝트는 단일 AI가 아닌, 각기 다른 전문성을 가진 에이전트들(데이터 분석, 뉴스 연구, 재무 분석)이 협업하여 시장을 다각도로 분석하고, 최적의 투자 리포트를 생성하는 것을 목표로 합니다.

## 🏗️ 시스템 아키텍처 (System Architecture)

본 프로젝트는 다음과 같은 계층적 멀티 에이전트 구조를 따릅니다.

1. **금융 코디네이터 (Financial Coordinator)**: 사용자의 투자 문의를 접수하고 하위 에이전트들에게 작업을 위임 및 조율합니다.
2. **데이터 분석가 (Data Analyst Agent)**: `yfinance`를 활용하여 실시간 시세, 기술적 지표(RSI, MACD 등), 과거 데이터를 분석합니다.
3. **뉴스 연구원 (News Researcher Agent)**: `Firecrawl API`를 통해 최신 뉴스, 시장 동향, 투자 심리를 파악합니다.
4. **재무 분석가 (Financial Analyst Agent)**: 기업의 재무제표(손익계산서, 대차대조표)를 기반으로 펀더멘털을 분석합니다.
5. **종합 분석 (Synthesis & Reporting)**: 각 에이전트의 결과를 종합하여 매수/매도/보유 의견이 담긴 최종 투자 보고서를 생성하고 저장합니다.

## 🛠️ 기술 스택 (Tech Stack)

* **Language**: Python 3.11+
* **Framework**: Google ADK (Agent Development Kit)
* **LLM**: Google Gemini (gemini-2.5-flash)
* **Data Source**:
    * Market Data: `yfinance`
    * News/Web: `Firecrawl` (Planned)
* **Tools**: Pandas, NumPy

## 환경 설정
프로젝트를 클론하고 가상 환경을 설정합니다(권장 사항).

### 가상 환경 생성
```bash
python -m venv .venv
```
### 가상 환경 활성화
**Windows**
```bash
.venv\Scripts\activate
```
**Mac/Linux**
```bash
source .venv/bin/activate
```

## 패키지 설치
필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

## 환경 변수 설정
프로젝트 루트에 .env 파일을 생성하고 Google API 키를 입력합니다.
```aiignore
# .env 파일
GOOGLE_API_KEY="your_api_key_here"
```

## 에이전트 실행
**터미널 환경**
```bash
adk run <agent_name>
```
**웹 환경**
```bash
adk web --port 8000
```