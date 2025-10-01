from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Simple Translator")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    q: str
    source: str = "ar"
    target: str = "bn"

class TranslationResponse(BaseModel):
    translatedText: str

@app.get("/")
async def root():
    return {"message": "Translation API is running!", "status": "active"}

@app.get("/languages")
async def get_languages():
    return [
        {"code": "ar", "name": "Arabic"},
        {"code": "bn", "name": "Bangla"}, 
        {"code": "en", "name": "English"}
    ]

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    # Simple translation simulation
    # In a real app, you'd integrate with a translation service
    arabic_to_bangla_map = {
        "بسم الله الرحمن الرحيم": "বিসমিল্লাহির রাহমানির রাহিম",
        "الحمد لله رب العالمين": "সমস্ত প্রশংসা আল্লাহর জন্য, যিনি সমগ্র বিশ্বজগতের প্রতিপালক",
        "الرحمن الرحيم": "পরম করুণাময়, অতি দয়ালু",
        "مالك يوم الدين": "বিচার দিনের মালিক",
        "إياك نعبد وإياك نستعين": "আমরা তোমারই ইবাদত করি এবং তোমারই কাছে সাহায্য চাই",
        "اهدنا الصراط المستقيم": "আমাদেরকে সরল পথ দেখাও",
        "صراط الذين أنعمت عليهم": "তাদের পথ যাদেরকে তুমি নেয়ামত দান করেছ",
        "غير المغضوب عليهم ولا الضالين": "তাদের পথ নয়, যাদের প্রতি তোমার গজব নাযিল হয়েছে এবং যারা পথভ্রষ্ট হয়েছে"
    }
    
    # Try to find exact matches first
    for arabic, bangla in arabic_to_bangla_map.items():
        if arabic in request.q:
            return TranslationResponse(translatedText=bangla)
    
    # Fallback: return the text with a note
    return TranslationResponse(
        translatedText=f"🌙 অনুবাদ পরিষেবা সক্রিয়\n\nআপনার আরবি টেক্সট: {request.q[:100]}...\n\n🔧 আসল অনুবাদ চালু করতে আমাদের একটি অনুবাদ সার্ভার সংযুক্ত করতে হবে।"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)