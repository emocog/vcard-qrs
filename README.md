# vcard-qrs

**FastAPI 기반 vCard(전자 명함) QR 코드 생성기**입니다.  
요청 시 SVG 및 PNG 형식의 QR 코드 이미지가 `qrs/` 디렉토리에 저장되며, GitHub Pages를 통해 웹에서 접근할 수 있습니다.

## 🚀 사용법

### 서버 실행

```bash
pip install fastapi uvicorn segno
uvicorn qr_server:app --host 0.0.0.0 --port 8000
```

### QR 생성 요청 예시

```
GET http://<서버IP>:8000/generate_vcard_qr?file_path=qrs/vcard_hong_at_emocog_com_kor.svg;name=길동;홍&displayname=홍길동&email=hong@emocog.com&phone=010-1234-5678&org=이모코그&title=연구원&url=https://emocog.com&workphone=02-1234-5678&format=png
```

## 📁 구조

```
qr_server.py          # FastAPI 서버 코드
qrs/                  # QR 코드 SVG 및 PNG 파일 저장 디렉토리
```

## 🌐 웹에서 사용

GitHub Pages를 설정하면 다음과 같은 URL로 접근 가능합니다:

- **SVG**:  
    `https://emocog.github.io/vcard-qrs/qrs/vcard_hong_at_emocog_com_kor.svg`
    
- **PNG**:  
    `https://emocog.github.io/vcard-qrs/qrs/vcard_hong_at_emocog_com_kor.png`
    

## 🧩 참고

- QR 코드 생성은 [Segno](https://github.com/heuer/segno) 사용
- QR 이미지는 **SVG**와 **PNG** 형식으로 각각 저장됩니다
- SVG/PNG 파일 이름은 이메일을 기반으로 자동 생성됩니다 (`@` → `_at_`, `.` → `_`)
