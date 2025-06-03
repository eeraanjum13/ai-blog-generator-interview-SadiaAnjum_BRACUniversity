from flask import Flask, request, jsonify
from ai_generator import generate_blog_post
from get_seo_data import get_seo_data
from apscheduler.schedulers.background import BackgroundScheduler
import os
from datetime import datetime

app = Flask(__name__)
saved_folder = "saved_posts"
os.makedirs(saved_folder, exist_ok=True)

def generate_and_save(keyword):
    print(f"[{datetime.now()}] Running blog generator for: {keyword}")
    try:
        seo_data = get_seo_data(keyword)
        content = generate_blog_post(keyword, seo_data)
        # content = '# Sample content for demonstration purposes\n'
        filename = f"{saved_folder}/{keyword.replace(' ', '_')}_{datetime.now().date()}.md"
        with open(filename, "w") as f:
            f.write(content)
        print(f"✅ Saved blog to: {filename}")
    except Exception as e:
        print(f"❌ Error in scheduler: {e}")


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'GET':
        keyword = request.args.get("keyword")
    elif request.method == 'POST':
        data = request.get_json()
        keyword = data.get("keyword") if data else None
    else:
        return jsonify({"error": "Unsupported method"}), 405

    if not keyword:
        return jsonify({"error": "keyword is required"}), 400

    seo_data = get_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)


    return jsonify({
        "keyword": keyword,
        "seo": seo_data,
        "blog_content": content
    })


# Schedule daily job
# scheduler = BackgroundScheduler()
# scheduler.add_job(lambda: generate_and_save("wireless earbuds"), "interval", seconds=20)
# scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
