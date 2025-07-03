from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from segno import helpers
import os
import re

app = FastAPI()

@app.get("/generate_vcard_qr")
def generate_vcard_qr(
    name: str = Query(...),
    displayname: str = Query(...),
    email: str = Query(...),
    phone: str = Query(...),
    org: str = Query(...),
    title: str = Query(...),
    url: str = Query(...),
    workphone: str = Query(...)
):
    
    # 파일 저장 위치
    os.makedirs("qrs", exist_ok=True)
    safe_name = email.replace("@", "_at_").replace(".", "_")
    filename = f"qrs/vcard_{safe_name}.svg"

    # VCard 기반 QR 코드 생성
    qr = helpers.make_vcard(
        name=name,
        displayname=displayname,
        email=email,
        phone=phone,
        org=org,
        title=title,
        url=url,
        workphone=workphone
    )

    # SVG로 저장
    qr.save(filename)

    return FileResponse(filename, media_type="image/svg+xml")
