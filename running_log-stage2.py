# === Stage 2: Проверка полей ===
# Project: RunningLog
def normalize_date(raw):
    if raw is None:
        raise ValueError("Дата не может быть пустой")
    text = raw.strip()
    if not text:
        raise ValueError("Дата не может быть пустой")
    candidate = text.replace(".", "/").replace("-", "/").replace(" ", "/")
    for fmt in ("%d/%m/%Y", "%Y/%m/%d", "%Y-%m-%d", "%d.%m.%Y"):
        try:
            return datetime.strptime(candidate, fmt).date()
        except ValueError:
            continue
    raise ValueError("Неверный формат даты, ожидаем дд/мм/гггг")


def normalize_distance(raw):
    if raw is None:
        raise ValueError("Дистанция не может быть пустой")
    text = raw.strip()
    if not text:
        raise ValueError("Дистанция не может быть пустой")
    try:
        distance = float(text)
    except ValueError:
        raise ValueError("Дистанция должна быть числом, например 5.2")
    if distance <= 0:
        raise ValueError("Дистанция должна быть больше нуля")
    return distance


def normalize_time(raw):
    if raw is None:
        raise ValueError("Время не может быть пустым")
    text = raw.strip()
    if not text:
        raise ValueError("Время не может быть пустым")
    if ":" in text:
        try:
            minutes, seconds = map(int, text.split(":"))
            if minutes < 0 or seconds < 0 or seconds >= 60:
                raise ValueError("Время должно быть в формате мм:сс")
            return timedelta(minutes=minutes, seconds=seconds)
        except ValueError:
            raise ValueError("Время должно быть в формате мм:сс, например 30:15")
    else:
        try:
            minutes = int(text)
            if minutes < 0:
                raise ValueError("Время не может быть отрицательным")
            return timedelta(minutes=minutes)
        except ValueError:
            raise ValueError("Время должно быть в минутах или формате мм:сс")


def normalize_shoes(raw):
    if raw is None:
        raise ValueError("Обувь не может быть пустой")
    text = raw.strip()
    if not text:
        raise ValueError("Обувь не может быть пустой")
    return text


def validate_run(run):
    errors = []
    try:
        run["date"] = normalize_date(run.get("date"))
    except ValueError as exc:
        errors.append("Дата: " + str(exc))
    try:
        run["distance"] = normalize_distance(run.get("distance"))
    except ValueError as exc:
        errors.append("Дистанция: " + str(exc))
    try:
        run["time"] = normalize_time(run.get("time"))
    except ValueError as exc:
        errors.append("Время: " + str(exc))
    try:
        run["shoes"] = normalize_shoes(run.get("shoes"))
    except ValueError as exc:
        errors
