import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code_and_title(prompt):
    system_prompt = (
        "Sen bir Python geliştirici yardımcısısın. "
        "Kullanıcının verdiği prompt'a göre, Python dilinde kod üretmelisin. "
        "Kodun içinde mutlaka verilen `Job` sınıfına uygun metotlar bulunmalı: `run()` ve `calculate_score()` metotları. "
        "Ayrıca, kullanıcıya bu kodun ne yaptığını özetleyen kısa bir başlık üret. "
        "Yanıt şu formatta olmalı:\n"
        "Başlık: <kısa başlık>\n\nKod:\n```python\n<kod burada>\n```"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # GPT-4 varsa onu da yazabilirsin
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )

        reply = response.choices[0].message['content']

        if "Başlık:" in reply and "```python" in reply:
            title = reply.split("Başlık:")[1].split("\n")[0].strip()
            code = reply.split("```python")[1].split("```")[0].strip()
        else:
            title = "Hata: Yanıt düzgün formatta alınamadı."
            code = "Hata: Yanıt düzgün formatta alınamadı."

    except Exception as e:
        title = "Hata: API isteği sırasında bir problem oluştu."
        code = f"Hata Detayı: {str(e)}"

    return title, code
