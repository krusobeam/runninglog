# === Stage 3: Хранилище в памяти ===
# Project: RunningLog
import threading


class InMemoryRunStore:
    def __init__(self):
        self._runs = {}
        self._counter = 0
        self._lock = threading.Lock()

    def add_run(self, run):
        with self._lock:
            self._counter += 1
            run.id = self._counter
            self._runs[run.id] = run
            return run.id

    def get_run(self, run_id):
        with self._lock:
            return self._runs.get(run_id)

    def list_runs(self):
        with self._lock:
            return list(self._runs.values())


class Run:
    def __init__(self, date, distance, time_seconds, shoe):
        self.id = None
        self.date = date
        self.distance = distance
        self.time_seconds = time_seconds
        self.shoe = shoe

    def __repr__(self):
        return f"Run(id={self.id}, date={self.date}, distance={self.distance}, " \
               f"time={self.time_seconds}, shoe={self.shoe})"


def pace(distance, time_seconds):
    if distance <= 0:
        return None
    return time_seconds / distance
