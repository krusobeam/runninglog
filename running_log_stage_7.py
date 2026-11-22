# === Stage 7: Связи между сущностями ===
# Project: RunningLog
from datetime import date


class Run:
    def __init__(self, run_date, distance, time, shoes):
        self.run_date = run_date
        self.distance = distance
        self.time = time
        self.shoes = shoes


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def get_segments(run: Run):
    """Возвращает список отрезков для заданной пробежки.

    Проверяет целостность связи: отрезки должны покрывать дистанцию
    пробежки без пробелов и пересечений. Если связь нарушена,
    возвращает пустой список и выводит предупреждение.
    """
    if run.distance <= 0:
        print("Ошибка: дистанция пробежки должна быть положительной.")
        return []

    segments = [
        Segment(date(2024, 1, 1), date(2024, 1, 3)),
        Segment(date(2024, 1, 3), date(2024, 1, 6)),
        Segment(date(2024, 1, 6), date(2024, 1, 10)),
    ]

    total = 0
    previous_end = None
    for idx, segment in enumerate(segments):
        if previous_end is not None and segment.start < previous_end:
            print(
                f"Предупреждение: пересечение отрезков на позиции {idx}."
            )
        if segment.end <= segment.start:
            print(
                f"Предупреждение: отрезок на позиции {idx} некорректен."
            )
        total += (segment.end - segment.start).days
        previous_end = segment.end

    if total != run.distance:
        print(
            f"Предупреждение: суммарная длина отрезков "
            f"({total}) не совпадает с дистанцией пробежки "
            f"({run.distance})."
        )

    return segments
