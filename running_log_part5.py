# === Stage 5: Удаление и восстановление ===
# Project: RunningLog
from datetime import datetime


class RunningLog:
    def __init__(self):
        self._runnings = {}
        self._trash = []
        self._counter = 1

    def add_running(self, date, distance, duration, shoe):
        key = f"run_{self._counter}"
        self._counter += 1
        self._runnings[key] = {
            "id": key,
            "date": date,
            "distance": distance,
            "duration": duration,
            "shoe": shoe,
            "deleted": False,
        }
        return key

    def soft_delete(self, run_id):
        running = self._runnings.get(run_id)
        if running and not running["deleted"]:
            self._trash.append(running)
            running["deleted"] = True
            del self._runnings[run_id]
            return True
        return False

    def restore(self, run_id):
        for item in self._trash:
            if item["id"] == run_id:
                self._runnings[run_id] = item
                item["deleted"] = False
                self._trash.remove(item)
                return True
        return False

    def list_runs(self):
        return [r for r in self._runnings.values() if not r["deleted"]]

    def list_trash(self):
        return list(self._trash)
