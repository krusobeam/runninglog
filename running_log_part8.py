# === Stage 8: Генерация идентификаторов ===
# Project: RunningLog
import uuid


PREFIX = "runlog"


def generate_unique_id() -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Формат: runlog_<короткий_уникальный_идентификатор>.
    """
    short_id = uuid.uuid4().hex[:8]
    unique_id = f"{PREFIX}_{short_id}"
    return unique_id


def is_unique(unique_id: str, existing_ids: set[str]) -> bool:
    """Проверяет, что идентификатор не совпадает с уже существующими.

    Args:
        unique_id: Кандидат на уникальный идентификатор.
        existing_ids: Множество уже используемых идентификаторов.

    Returns:
        True если идентификатор уникален, иначе False.
    """
    return unique_id not in existing_ids


def generate_unique_id_with_check(
    existing_ids: set[str],
) -> str:
    """Генерирует уникальный идентификатор с проверкой коллизий.

    Если сгенерированный идентификатор уже используется, создаётся новый,
    пока не будет найден уникальный вариант.

    Args:
        existing_ids: Множество уже используемых идентификаторов.

    Returns:
        Уникальный идентификатор с префиксом проекта.
    """
    while True:
        candidate = generate_unique_id()
        if is_unique(candidate, existing_ids):
            return candidate


def main() -> None:
    """Демонстрация работы генерации уникальных идентификаторов."""
    ids: set[str] = set()

    first_id = generate_unique_id_with_check(ids)
    print(f"Сгенерирован первый идентификатор: {first_id}")
    ids.add(first_id)

    for _ in range(5):
        new_id = generate_unique_id_with_check(ids)
        print(f"Сгенерирован новый идентификатор: {new_id}")
        ids.add(new_id)

    print(f"Всего сгенерировано идентификаторов: {len(ids)}")


if __name__ == "__main__":
    main()
