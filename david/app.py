from flask import Flask, render_template, request
from gtts import gTTS
import io
import base64
from datetime import datetime

app = Flask(__name__)

VALID_LANGS = {"ko", "en", "ja", "es"}

@app.route("/", methods=["GET", "POST"]) # 루트 경로에 get post 요청 허용
def index():
    error = None 
    audio = None

    if request.method == "GET": # 클라이언트의 접속, 새로고침 시 요청 -> 기본 페이지 제공
        return render_template("index.html", error=error, audio=audio)

    if request.method == "POST": # 클라이언트의 post 요청시 처리 구문
        input_text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", "").strip()

        if not input_text:
            error = "텍스트를 입력해주세요."
        elif lang not in VALID_LANGS:
            error = "지원하지 않는 언어입니다."
        else:
            try:
                tts = gTTS(text=input_text, lang=lang)
                buf = io.BytesIO()
                tts.write_to_fp(buf)
                buf.seek(0) # 버퍼의 읽기 시작점 고정, 새로 생성된 오디오 파일을 읽기 가능
                audio = base64.b64encode(buf.read()).decode("utf-8")

                # 입력 로그 저장
                with open("david/input_log.txt", "a", encoding="utf-8") as f:
                    f.write(f"[{datetime.now()}] {input_text} ({lang})\n")

            except Exception as e:
                error = f"TTS 변환 중 오류 발생: {e}"

        return render_template("index.html", error=error, audio=audio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
