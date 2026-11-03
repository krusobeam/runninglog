# === Stage 1: Каркас модуля ===
# Project: RunningLog
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Running:
    date: date
    distance: float
    time: float
    shoes: Optional[str] = None


def create_demo_records() -> List[Running]:
    return [
        Running(date(2024, 1, 5), 5.0, 28.5, "Adidas Adizero"),
        Running(date(2024, 1, 12), 10.0, 58.0, "Nike Pegasus"),
        Running(date(2024, 1, 19), 3.2, 22.0),
    ]


def main() -> None:
    records = create_demo_records()
    print("Беговой дневник RunningLog")
    print("=" * 30)
    for record in records:
        speed = record.distance / (record.time / 60)
        print(f"Дата: {record.date}, Дистанция: {record.distance} км, "
              f"Время: {record.time} мин, Обувь: {record.shoes}, "
              f"Темп: {speed:.1f} мин/км")


if __name__ == "__main__":
    main()
