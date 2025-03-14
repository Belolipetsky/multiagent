import json
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

LOG_FILE = "data/outputs/logs.json"

llm = OpenAI(api_key=OPENAI_API_KEY, model_name=MODEL_NAME, temperature=TEMPERATURE)

def run_analysis_chain() -> str:
    # Чтение логов из файла
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except Exception as e:
        return f"Ошибка при чтении логов: {e}"
    
    template = """
Ты являешься модулем анализа. На основе следующих логов действий:
{logs}
сформируй структурированный анализ:
- Общая последовательность действий
- Оценка эффективности (например, количество шагов, соответствие целям)
- Рекомендации по улучшению взаимодействия

Выведи результат в виде структурированного JSON.
    
Вывод (JSON):
"""
    prompt = PromptTemplate(template=template, input_variables=["logs"])
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(logs=json.dumps(logs, ensure_ascii=False, indent=2))
    return result.strip()
