import json
import os

LOG_FILE = "data/outputs/logs.json"

def log_step(step_data: dict):
    # Создаем директорию для логов, если не существует
    log_dir = os.path.dirname(LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Загружаем существующие логи, если файл уже есть
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    else:
        logs = []
    # Добавляем новый шаг
    logs.append(step_data)
    # Сохраняем обновленные логи
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)
