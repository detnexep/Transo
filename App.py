from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Arabic to Bangla Translator API", "status": "active"})

@app.route('/languages', methods=['GET'])
def languages():
    return jsonify([
        {"code": "ar", "name": "Arabic"},
        {"code": "bn", "name": "Bangla"},
        {"code": "en", "name": "English"}
    ])

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('q', '')
    
    # Simple translation mapping
    translations = {
        "بسم الله الرحمن الرحيم": "বিসমিল্লাহির রাহমানির রাহিম",
        "الحمد لله رب العالمين": "সমস্ত প্রশংসা আল্লাহর জন্য, যিনি সমগ্র বিশ্বজগতের প্রতিপালক",
        "الرحمن الرحيم": "পরম করুণাময়, অতি দয়ালু",
        "مالك يوم الدين": "বিচার দিনের মালিক",
        "إياك نعبد وإياك نستعين": "আমরা তোমারই ইবাদত করি এবং তোমারই কাছে সাহায্য চাই",
        "اهدنا الصراط المستقيم": "আমাদেরকে সরল পথ দেখাও",
        "الله": "আল্লাহ",
        "رب": "প্রতিপালক",
        "العالمين": "বিশ্বজগত"
    }
    
    # Replace common phrases
    translated_text = text
    for arabic, bangla in translations.items():
        translated_text = translated_text.replace(arabic, bangla)
    
    return jsonify({"translatedText": translated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
