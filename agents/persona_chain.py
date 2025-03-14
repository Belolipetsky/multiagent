from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = OpenAI(api_key=OPENAI_API_KEY, model_name=MODEL_NAME, temperature=TEMPERATURE)

def run_persona_chain(analysis_result: str, persona_description: str, task_description: str) -> str:
    template = """
Ты являешься модулем генерации действий персонажа. 
    
Даны следующие данные:
- Описание интерфейса: {analysis_result}
- Описание персонажа: {persona_description}
- Описание задачи: {task_description}

Сгенерируй последовательность действий, которые персонаж выполнит для достижения поставленной задачи. Для каждого шага опиши:
- Конкретное действие с ПИ (например, "нажать кнопку 'Войти'")
- Мысли и эмоции персонажа
    
Форматируй вывод в виде структурированного JSON.
    
Пример:
{
  "steps": [
    {
      "action": "click",
      "target": "Кнопка 'Войти'",
      "thoughts": "Я уверен, что это правильное решение",
      "emotions": "уверенность"
    },
    ...
  ]
}
    
Вывод (JSON):
"""
    prompt = PromptTemplate(
        template=template,
        input_variables=["analysis_result", "persona_description", "task_description"]
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(
        analysis_result=analysis_result,
        persona_description=persona_description,
        task_description=task_description
    )
    return result.strip()
