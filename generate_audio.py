import os, base64, json, httpx

API_KEY = "tp-cs17d3gwyvri570hxbikfvg7wh8tuma0oheup8x8opozayir"
BASE_URL = "https://api.xiaomimimo.com/v1/chat/completions"

pages = [
    "I want a party.",
    "I want some cards.",
    "I want some gifts.",
    "I want some balloons.",
    "I want some cupcakes.",
    "I want some toys.",
    "Party time!",
    "Thank you, Elephant."
]

style = "Gentle, warm, and soothing female voice speaking slowly to young children. Clear pronunciation, loving and encouraging tone, like a mother reading a bedtime story. Speak at a slow pace with slight pauses between phrases."

audio_dir = os.path.join(os.path.dirname(__file__), "assets", "audio")
os.makedirs(audio_dir, exist_ok=True)

headers = {"api-key": API_KEY, "Content-Type": "application/json"}

for i, text in enumerate(pages):
    print(f"Generating page {i+1}: {text}")
    body = {
        "model": "mimo-v2.5-tts",
        "messages": [
            {"role": "user", "content": style},
            {"role": "assistant", "content": text}
        ],
        "audio": {"format": "wav", "voice": "Mia"}
    }
    try:
        r = httpx.post(BASE_URL, headers=headers, json=body, timeout=60)
        print(f"  Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            audio_b64 = data["choices"][0]["message"]["audio"]["data"]
            audio_bytes = base64.b64decode(audio_b64)
            filepath = os.path.join(audio_dir, f"page{i+1}.wav")
            with open(filepath, "wb") as f:
                f.write(audio_bytes)
            print(f"  Saved: {filepath} ({len(audio_bytes)} bytes)")
        else:
            print(f"  Error: {r.text[:200]}")
    except Exception as e:
        print(f"  Exception: {e}")

print("Done!")