from flask import Flask, render_template
import makejson

app = Flask(__name__)

@app.route('/')
def index():
    # 예시 JSON 데이터 생성
    json_data=makejson.jjsonpy()
    
    return render_template('index.html', json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
