import json

from agents.image_analysis_chain import run_image_analysis
from agents.persona_chain import run_persona_chain
from agents.modeling_chain import run_modeling_chain
from agents.logging_chain import log_step
from agents.analysis_chain import run_analysis_chain
from agents.prompt_rules_chain import get_prompt_rules

def main():
    # Пример входных данных (в реальном проекте можно загружать из файлов)
    ui_description = (
        "Интерфейс содержит кнопку 'Войти', поле для ввода логина, поле для ввода пароля, "
        "а также ссылку 'Регистрация'."
    )
    task_description = "Пользователь должен войти в систему, используя корректные учетные данные."
    persona_description = "Пользователь – опытный интернет-пользователь, уверенный в своих действиях."
    
    # 1. Анализ изображения (ПИ)
    image_analysis = run_image_analysis(ui_description)
    print("Анализ изображения:", image_analysis)
    
    # Сохраним шаг в лог
    step1 = {
        "step": 1,
        "module": "image_analysis_chain",
        "input": ui_description,
        "output": image_analysis
    }
    log_step(step1)
    
    # 2. Получение правил промтов (при необходимости)
    prompt_rules = get_prompt_rules()
    print("Правила промтов:", prompt_rules)
    
    # 3. Генерация действий персонажа (с учетом описания интерфейса, задачи и персонажа)
    persona_actions = run_persona_chain(image_analysis, persona_description, task_description)
    print("Действия персонажа:", persona_actions)
    
    step2 = {
        "step": 2,
        "module": "persona_chain",
        "input": {
            "image_analysis": image_analysis,
            "persona_description": persona_description,
            "task_description": task_description
        },
        "output": persona_actions
    }
    log_step(step2)
    
    # 4. Моделирование: проверка валидности действий и обновление состояния интерфейса
    updated_ui_state = run_modeling_chain(persona_actions, image_analysis)
    print("Обновленное состояние интерфейса:", updated_ui_state)
    
    step3 = {
        "step": 3,
        "module": "modeling_chain",
        "input": {
            "persona_actions": persona_actions,
            "image_analysis": image_analysis
        },
        "output": updated_ui_state
    }
    log_step(step3)
    
    # 5. Анализ логов и формирование отчёта
    analysis_report = run_analysis_chain()
    print("Отчёт анализа:", analysis_report)
    
    step4 = {
        "step": 4,
        "module": "analysis_chain",
        "input": "Логи из файла",
        "output": analysis_report
    }
    log_step(step4)
    
    # Сохраняем финальный отчёт в отдельном файле
    with open("data/outputs/analysis_report.json", "w", encoding="utf-8") as f:
        json.dump(json.loads(analysis_report), f, indent=2, ensure_ascii=False)
    
if __name__ == "__main__":
    main()
