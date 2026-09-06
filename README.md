# 학계산 v1.0

정적 HTML/CSS/JS로 만든 학생용 성적·시험 계산기 사이트입니다. 서버나 빌드 과정 없이 배포할 수 있습니다.

## 배포 전 필수 1가지
현재 canonical URL과 sitemap에 `https://reridy.github.io`가 들어 있습니다. 배포 후 받은 주소(예: `https://hakcalc.pages.dev`)로 프로젝트 전체에서 문자열을 일괄 변경하세요.

VS Code: Ctrl+Shift+H → `https://reridy.github.io` 검색 → 실제 주소로 Replace All.

## 무료 배포
GitHub 저장소에 이 폴더 내용을 올린 뒤 Cloudflare Pages/GitHub Pages/정적 호스팅에 연결할 수 있습니다. 루트 디렉터리가 사이트 루트가 되도록 설정하세요.

## 검색 등록
1. GitHub Pages 배포 확인
2. Google Search Console에 `https://reridy.github.io/` 등록
3. `https://reridy.github.io/sitemap.xml` 제출
4. 주요 5개 계산기 URL 색인 요청

## 분석/광고
아직 분석 스크립트와 실제 광고 코드는 넣지 않았습니다. 개인정보처리방침도 현재 상태에 맞게 작성되어 있습니다. 분석 또는 광고 서비스를 추가할 때 privacy.html을 함께 갱신해야 합니다.

## 파일
- index.html: 홈
- grade-5.html: 내신 5등급 계산
- exam-target.html: 기말 목표점수
- weighted-score.html: 수행 포함 최종점수
- target-average.html: 목표 평균
- grade-boundary.html: 등급 경계 인원
- about.html / privacy.html
- robots.txt / sitemap.xml
- assets/style.css / assets/app.js
