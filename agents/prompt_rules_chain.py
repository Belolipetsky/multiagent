def get_prompt_rules() -> dict:
    rules = {
         "allowed_actions": ["click", "input_text", "navigate", "scroll"],
         "validation_message": (
             "Действие должно соответствовать допустимому набору: click, input_text, navigate, scroll."
         )
    }
    return rules
