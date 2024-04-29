class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            raise ValueError("Worker must be an instance of Worker class")

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            raise ValueError("Boss must be an instance of Boss class")


# Example usage
boss1 = Boss(1, "Boss1", "Company1")
boss2 = Boss(2, "Boss2", "Company2")
worker1 = Worker(1, "Worker1", "Company1", boss1)
worker2 = Worker(2, "Worker2", "Company2", boss2)

# Adding workers to boss
boss1.add_worker(worker1)
boss2.add_worker(worker2)
print("Boss1's workers:", [worker.name for worker in boss1.workers])
print("Boss2's workers:", [worker.name for worker in boss2.workers])

# Trying to set boss of worker1 to boss2
try:
    worker1.boss = boss2
    print("Worker1's boss:", worker1.boss.name)
except ValueError as e:
    print(e)
