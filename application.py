from flask import Flask
from datetime import datetime

app = Flask(__name__)

# 學號與姓名（已依你的資訊設定）
STUDENT_ID = "s1121432"
STUDENT_NAME = "張嘉祥"

@app.route("/")
def index():
    now_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>HW3 PaaS - {STUDENT_ID} {STUDENT_NAME}</title>
</head>
<body>
    <h1>雲端 PaaS 網站作業</h1>
    <p>學號姓名：{STUDENT_ID} {STUDENT_NAME}</p>
    <p>首頁執行當下的伺服器時間（UTC）：{now_utc}</p>
</body>
</html>"""
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
