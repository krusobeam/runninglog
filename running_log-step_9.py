# === Stage 9: Фильтрация записей ===
# Project: RunningLog
def filter_runs_by_distance(runs, min_distance=None, max_distance=None):
    result = []
    for run in runs:
        distance = run.get("distance")
        if distance is None:
            continue
        if min_distance is not None and distance < min_distance:
            continue
        if max_distance is not None and distance > max_distance:
            continue
        result.append(run)
    return result


def filter_runs_by_date_range(runs, start_date=None, end_date=None):
    result = []
    for run in runs:
        run_date = run.get("date")
        if start_date is not None and run_date < start_date:
            continue
        if end_date is not None and run_date > end_date:
            continue
        result.append(run)
    return result


def filter_runs(runs, min_distance=None, max_distance=None,
                 start_date=None, end_date=None):
    filtered = runs
    if min_distance is not None or max_distance is not None:
        filtered = filter_runs_by_distance(filtered, min_distance, max_distance)
    if start_date is not None or end_date is not None:
        filtered = filter_runs_by_date_range(filtered, start_date, end_date)
    return filtered


def find_runs_near_target_distance(runs, target_distance, tolerance=0.1):
    result = []
    for run in runs:
        distance = run.get("distance")
        if distance is None:
            continue
        if abs(distance - target_distance) <= distance * tolerance:
            result.append(run)
    return result


def find_runs_in_week(runs, reference_date, days=7):
    from datetime import timedelta
    start = reference_date - timedelta(days=days)
    end = reference_date + timedelta(days=1)
    return filter_runs_by_date_range(runs, start, end)
