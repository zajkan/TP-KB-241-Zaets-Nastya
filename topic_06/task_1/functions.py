LOG_FILE = "calculator_log.txt"

def log_cust(oper, a, b, result=None, error=None):
    
    if error:
        log_level = "ERROR"
        status = f"Помилка: {error}"
    else:
        log_level = "INFO"
        status = f"Результат: {result}"
    log_enter = f"{log_level} - Операція: {a} {oper} {b}, {status}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_enter)

def add(a, b):
    result = a + b
    log_cust("+", a, b, result)
    return result

def subt(a, b):
    result = a - b
    log_cust("-", a, b, result)
    return result

def multi(a, b):
    result = a * b
    log_cust("*", a, b, result)
    return result

def div(a, b):
    try:
        result = a / b
        log_cust("/", a, b, result)
        return result
    except ZeroDivisionError:
        error_msg ="Помилка ділення на 0 неможливе!\n"
        print(error_msg)
        log_cust("/", a, b, error=error_msg)
        return 