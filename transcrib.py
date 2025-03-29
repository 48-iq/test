import torch
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline, logging
from datasets import load_dataset

logging.set_verbosity_error()  


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

audio_path = "./testcall.mp3"
audio, sr = librosa.load(audio_path, sr=16000) 


result = pipe(audio, return_timestamps=True)
print(result["text"])


timestamps = result["chunks"]

# Вычисляем паузы между словами/сегментами
pauses = []
for i in range(1, len(timestamps)):
    prev_end = timestamps[i-1]["timestamp"][1]  # конец предыдущего слова
    current_start = timestamps[i]["timestamp"][0]  # начало текущего слова
    pause = current_start - prev_end
    if pause > 0.5:  # учитываем только положительные паузы
        pauses.append(pause)

# Вычисляем среднюю длину пауз
if pauses:
    average_pause = sum(pauses) / len(pauses)
    print(f"Средняя длина пауз: {average_pause:.2f} секунд")
    print(f"Количество пауз: {len(pauses)}")
    print(f"Максимальная длина пауз: {max(pauses):.2f} секунд")
else:
    print("Пауз не обнаружено.")