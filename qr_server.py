from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from segno import helpers
import os

app = FastAPI()

@app.get("/generate_vcard_qr")
def generate_vcard_qr(
    file_path: str = Query (...),
    name: str = Query(...),
    displayname: str = Query(...),
    email: str = Query(...),
    phone: str = Query(...),
    org: str = Query(...),
    title: str = Query(...),
    url: str = Query(...),
    workphone: str = Query(...),
    format: str = Query("png", regex="^(png|svg)$")  # format 파라미터 추가
):
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

    # SVG 또는 PNG 저장 및 응답
    if format == "svg":
        qr.save(file_path, kind="svg")
        return FileResponse(file_path, media_type="image/svg+xml")
    else:
        qr.save(file_path, kind="png", scale=5)
        return FileResponse(file_path, media_type="image/png")
