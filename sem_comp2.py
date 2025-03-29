import requests
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import json
import 

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload={
  'scope': 'GIGACHAT_API_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '6904a87d-4909-455d-8b87-33269a26c04e',
  'Authorization': 'Basic N2Q0Y2Y3MTQtMjZiZS00ZTUxLWFhMDQtM2I0Y2VlNmVmYTg2OjEzMWU4YTIyLTAxNzYtNDVlMi05NjY5LTUyNzEyNmFkMjcwNQ=='
}

authkey = 'Basic N2Q0Y2Y3MTQtMjZiZS00ZTUxLWFhMDQtM2I0Y2VlNmVmYTg2OjEzMWU4YTIyLTAxNzYtNDVlMi05NjY5LTUyNzEyNmFkMjcwNQ=='

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
print(response.text)


# Конфигурация
API_KEY = response.json()["access_token"]
TRANSCRIPT = """Транскрибированный текст звонка здесь..."""

CRITERIA = [
    "Указал имя компании в начале разговора - company",
    "Представился по имени - name",
    "Уточнил потребности клиента - needs",
    "Озвучил сроки выполнения задачи - deadline",
    "Поблагодарил за обращение - gratitude",
    "Использовал стандартные фразы компании - standard_phrases",
    "Предложил дополнительную помощь - additional_help"
]

def analyze_call(transcript: str, criteria: list) -> dict:
    
    # Формируем промпт
    system_prompt = f"""
    Проанализируй текст разговора менеджера с клиентом.
     
    Для каждого критерия из списка верни JSON-объект с полем "result" (true/false).
    Также оцени тон звонка (от 1 до 5, где 5 - отличный, а 1 - ужасный) и верни JSON-объект с полем "tone".
    После дай рекомендацию по критериям и тону звонка, для каждой рекомендации верни JSON-объект с полем "recommendation".
    Критерии: {", ".join(criteria)}
    
    Пример ответа: 
    {{
        "competitions":{{
          "company": {{"result": true}},
          "name": {{"result": false}}
          "tone: {{"tone": 3}},
        }},
        "tone: {{"tone": 3}},
        "recommendations": [
            {{"recommendation": "Рекомендация 1"}}, 
            {{"recommendation": "Рекомендация 2"}}
        ]
    }}
    """

    print("system prompt:", system_prompt)
    
    # Формируем запрос
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }
    
    data = {
        "model": "GigaChat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transcript}
        ],
        "temperature": 0.1  # Для большей детерминированности
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print("response:", response.json())
    response.raise_for_status()
    
    # Парсинг ответа
    result = response.json()["choices"][0]["message"]["content"]
    print("result:", result)
    return json.loads(result)

TRANSCRIPT = ""

with open('textcall.txt', 'r', encoding='utf-8') as f:
    TRANSCRIPT = f.read()

# Запуск анализа
if __name__ == "__main__":
    analysis = analyze_call(TRANSCRIPT, CRITERIA)

    




