# === Stage 6: Связанная сущность ===
# Project: RunningLog
from datetime import datetime


class Segment:
    def __init__(self, distance, pace, notes=""):
        if distance <= 0:
            raise ValueError("Дистанция должна быть положительной")
        if pace <= 0:
            raise ValueError("Темп должен быть положительным")
        self.distance = distance
        self.pace = pace
        self.notes = notes

    def time(self):
        return self.distance * self.pace

    def __repr__(self):
        return f"Segment(distance={self.distance}, pace={self.pace})"


class Runner:
    def __init__(self, name):
        self.name = name
        self.runs = []

    def add_run(self, date, distance, time, shoes):
        run = Run(date, distance, time, shoes)
        self.runs.append(run)
        return run


class Run:
    def __init__(self, date, distance, time, shoes):
        self.date = date
        self.distance = distance
        self.time = time
        self.shoes = shoes
        self.segments = []

    def add_segment(self, segment):
        self.segments.append(segment)

    def total_distance(self):
        return sum(seg.distance for seg in self.segments)

    def total_pace(self):
        total = sum(seg.distance for seg in self.segments)
        return total / len(self.segments) if self.segments else 0


def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError("Неверный формат даты")


def average_pace(distance, time_seconds):
    if distance <= 0:
        raise ValueError("Дистанция должна быть положительной")
    return time_seconds / distance


def split_into_segments(distance, pace):
    segments = []
    for i in range(1, int(distance) + 1):
        segments.append(Segment(distance / (i + 1), pace))
    return segments
