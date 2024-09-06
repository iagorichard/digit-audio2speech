from fastapi import FastAPI, UploadFile, File, HTTPException
import speech_recognition as sr
import io
from numbers_map import numbers_map  # Importando o dicionário do arquivo numbers_map.py

app = FastAPI()

# Função para mapear palavras a dígitos
def convert_to_digits(text):
    words = text.split()
    digits = [numbers_map.get(word.lower(), word) for word in words]
    return ''.join(digits)

# Endpoint que recebe o áudio e converte para dígitos
@app.post("/convert-audio-to-digits/")
async def convert_audio_to_digits(file: UploadFile = File(...)):
    print(f"Tipo de arquivo recebido: {file.content_type}")
    print(f"Nome do arquivo: {file.filename}")
    
    if file.content_type not in ["audio/wav", "audio/x-wav"]:
        raise HTTPException(status_code=400, detail="Apenas arquivos .wav são suportados.")
    
    recognizer = sr.Recognizer()

    try:
        # Ler o conteúdo do arquivo de áudio
        audio_data = await file.read()
        print(f"Tamanho do arquivo de áudio recebido: {len(audio_data)} bytes")
        
        with sr.AudioFile(io.BytesIO(audio_data)) as source:
            audio_content = recognizer.record(source)
            print("Áudio processado com sucesso.")

        # Reconhecer fala em português brasileiro
        text = recognizer.recognize_google(audio_content, language="pt-BR")
        print("Texto reconhecido:", text)

        # Converter palavras em dígitos
        digits = convert_to_digits(text)
        return {"original_text": text, "converted_digits": digits}

    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Não foi possível entender o áudio. Tente com um áudio mais claro ou longo.")
    except sr.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao serviço de reconhecimento de fala: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail=str(e))
