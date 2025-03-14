from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = OpenAI(api_key=OPENAI_API_KEY, model_name=MODEL_NAME, temperature=TEMPERATURE)

def run_image_analysis(ui_description: str) -> str:
    template = """
Ты являешься модулем анализа пользовательского интерфейса. 
На вход поступает описание интерфейса: {ui_description}. 
Выдели ключевые компоненты (например, кнопки, поля ввода, меню) и сформируй структурированный JSON-объект, описывающий эти элементы.
    
Пример вывода:
{
  "buttons": ["Войти"],
  "input_fields": ["логин", "пароль"],
  "links": ["Регистрация"]
}
    
Вывод (JSON):
"""
    prompt = PromptTemplate(template=template, input_variables=["ui_description"])
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(ui_description=ui_description)
    return result.strip()
