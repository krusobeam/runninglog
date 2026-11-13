# === Stage 4: Редактирование записей ===
# Project: RunningLog
from dataclasses import dataclass, field
from datetime import date


ALLOWED_RUN_FIELDS = ("date", "distance", "duration", "shoes")

FIELD_TYPES = {
    "date": date,
    "distance": float,
    "duration": float,
    "shoes": str,
}


@dataclass
class Run:
    date: date
    distance: float
    duration: float
    shoes: str


def is_valid_value(field_name, value):
    expected = FIELD_TYPES.get(field_name)
    if expected is None:
        return False
    return isinstance(value, expected)


def filter_run_updates(changes):
    filtered = {}
    for key, value in changes.items():
        if key in ALLOWED_RUN_FIELDS:
            if is_valid_value(key, value):
                filtered[key] = value
    return filtered


def update_run(run, changes):
    if not isinstance(changes, dict):
        raise ValueError("изменения должны быть словарём")

    filtered = filter_run_updates(changes)

    new_date = filtered.get("date", run.date)
    new_distance = filtered.get("distance", run.distance)
    new_duration = filtered.get("duration", run.duration)
    new_shoes = filtered.get("shoes", run.shoes)

    return Run(new_date, new_distance, new_duration, new_shoes)


def find_run_by_id(runs, run_id):
    for run in runs:
        if run.id == run_id:
            return run
    return None


def edit_run_by_id(runs, run_id, changes):
    target = find_run_by_id(runs, run_id)
    if target is None:
        raise ValueError(f"пробежка с идентификатором {run_id} не найдена")

    updated = update_run(target, changes)

    for index, run in enumerate(runs):
        if run.id == run_id:
            runs[index] = updated
            break

    return target, updated
