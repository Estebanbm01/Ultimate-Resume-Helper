import google.generativeai as genai

# Your API key
genai.configure(api_key="AIzaSyAUznpVqGIjGu7qinINqNHBg10WXnXbhUw")

print("🔍 Checking available Gemini models...\n")

try:
    # List all available models
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✅ Model: {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print()
except Exception as e:
    print(f"❌ Error: {e}")