from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

llm = OpenAI(api_key=OPENAI_API_KEY, model_name=MODEL_NAME, temperature=TEMPERATURE)

def run_modeling_chain(persona_actions: str, image_analysis: str) -> str:
    template = """
Ты являешься модулем моделирования взаимодействия с пользовательским интерфейсом. 
На вход получены следующие данные:
- Действия персонажа: {persona_actions}
- Текущее описание интерфейса: {image_analysis}

Проверь валидность действий персонажа с учетом допустимых правил.
Если какое-либо действие не соответствует правилам, сообщи об ошибке.
Если все действия валидны, сформируй обновленное описание интерфейса в виде структурированного JSON.
    
Вывод (JSON):
"""
    prompt = PromptTemplate(template=template, input_variables=["persona_actions", "image_analysis"])
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(persona_actions=persona_actions, image_analysis=image_analysis)
    return result.strip()
