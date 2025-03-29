from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Загрузка модели и токенизатора
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=2)

# Пример функций для анализа каждого критерия
def check_criterion(text, question):
    # Формируем входные данные для модели
    inputs = tokenizer(question, text, return_tensors="pt", truncation=True, max_length=512)
    
    # Получаем предсказание
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Интерпретируем результат
    predicted_class = torch.argmax(outputs.logits).item()
    return bool(predicted_class)

# Анализ по каждому критерию
def analyze_transcript(transcript):
    results = {
        '1. Уточнил имя клиента': False,
        '2. Назвал свое имя и компанию': False,
        '3. Уточнил сферу деятельности клиента': False,
        '4. Выявление ЛПР и ЛВПР': False,
        '5. Озвучивает информационные поводы': False
    }
    
    # Проверка каждого критерия (упрощённые вопросы для примера)
    results['1. Уточнил имя клиента'] = check_criterion(transcript, "уточнить имя клиента")
    results['2. Назвал свое имя и компанию'] = check_criterion(transcript, "назвал имя и компанию")
    results['3. Уточнил сферу деятельности клиента'] = check_criterion(transcript, "сфера деятельности")
    results['4. Выявление ЛПР и ЛВПР'] = check_criterion(transcript, "подбор запчастей")
    results['5. Озвучивает информационные поводы'] = check_criterion(transcript, "CRM система")
    
    return results

transcript = ""

with open('textcall.txt', 'r', encoding='utf-8') as f:
    transcript = f.read()

# Пример использования
analysis_results = analyze_transcript(transcript)
for criterion, result in analysis_results.items():
    print(f"{criterion}: {'Да' if result else 'Нет'}")