from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ TikTok Auto Uploader is LIVE!"

@app.route('/upload', methods=['POST'])
def upload_tiktok():
    try:
        data = request.json
        
        video_url = data.get('video_url', '')
        script = data.get('script', '')
        email = data.get('email', 'jhfflfbvffgh@gmail.com')
        
        print(f"🎥 جاري معالجة الفيديو: {video_url}")
        
        time.sleep(2)
        
        return jsonify({
            "status": "success",
            "message": "تم استلام بيانات الفيديو بنجاح!",
            "tiktok_url": "https://tiktok.com/@your_video/12345",
            "received_data": {
                "video": video_url,
                "script": script,
                "account": email
            }
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": f"خطأ: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
