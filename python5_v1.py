from abc import ABC, abstractmethod


class CrewMember(ABC):
    def __init__(self, name, rank, health=100, energy=100):
        self.name = name
        self.rank = rank
        self.health = health
        self.energy = energy

    @abstractmethod
    def work(self):
        pass

    def rest(self):
        self.energy = min(100, self.energy + 20)
        self.health = min(100, self.health + 10)
        print(f"{self.rank} {self.name} отдыхает. (+10 здоровье, +20 энергия)")

    def status_report(self):
        return f"{self.rank} {self.name} | Здоровье: {self.health}, Энергия: {self.energy}"


class Engineer(CrewMember):
    def __init__(self, name, rank, repair_skill, health=100, energy=100):
        super().__init__(name, rank, health, energy)
        self.repair_skill = repair_skill

    def work(self):
        self.energy -= 20
        self.health -= 10
        print(f"{self.rank} {self.name} чинит системы (навык {self.repair_skill}).")


class Pilot(CrewMember):
    def __init__(self, name, rank, flight_hours, health=100, energy=100):
        super().__init__(name, rank, health, energy)
        self.flight_hours = flight_hours

    def work(self):
        self.energy -= 20
        self.health -= 5
        print(f"{self.rank} {self.name} управляет кораблём (налёт {self.flight_hours} часов).")


class Scientist(CrewMember):
    def __init__(self, name, rank, research_field, health=100, energy=100):
        super().__init__(name, rank, health, energy)
        self.research_field = research_field

    def work(self):
        self.energy -= 10
        self.health -= 12
        print(f"{self.rank} {self.name} проводит исследование в области: {self.research_field}.")


class Spacecraft:
    def __init__(self, name, ship_type, crew_capacity, hull_integrity=100):
        self.name = name
        self.ship_type = ship_type
        self.crew_capacity = crew_capacity
        self.current_crew = []
        self.hull_integrity = hull_integrity

    def add_crew_member(self, crew_member):
        if len(self.current_crew) < self.crew_capacity:
            self.current_crew.append(crew_member)
            print(f"{crew_member.rank} {crew_member.name} назначен на корабль {self.name}.")
        else:
            print("Экипаж корабля полон!")

    def remove_crew_member(self, crew_member):
        if crew_member in self.current_crew:
            self.current_crew.remove(crew_member)
            print(f"{crew_member.rank} {crew_member.name} покинул корабль {self.name}.")

    def launch_mission(self, destination):
        print(f"🚀 Корабль {self.name} отправляется на миссию в {destination}!")


class SpaceStation:
    def __init__(self, name):
        self.name = name
        self.crew = []
        self.spacecraft_fleet = []
        self.resources = {"еда": 100, "вода": 100, "кислород": 100}

    def add_crew_member(self, crew_member):
        self.crew.append(crew_member)
        print(f"{crew_member.rank} {crew_member.name} прибыл на станцию {self.name}.")

    def assign_crew_to_ship(self, crew_members, spacecraft):
        for member in crew_members:
            if member in self.crew:
                spacecraft.add_crew_member(member)

    def daily_operations(self):
        print(f"🌌 На станции {self.name} выполняются ежедневные операции.")
        for res in self.resources:
            self.resources[res] -= 10

    def generate_report(self):
        print(f"\n📊 === Отчёт о станции {self.name} ===")
        print("Экипаж станции:")
        for member in self.crew:
            print(" ", member.status_report())

        print("\nФлот кораблей:")
        for ship in self.spacecraft_fleet:
            print(f"  {ship.name} ({ship.ship_type}), экипаж: {len(ship.current_crew)}")

        print("\nРесурсы:")
        for key, value in self.resources.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    station = SpaceStation("Орбита-5")

    eng = Engineer("Ладыгин", "Лейтенант", repair_skill=75, health=90, energy=65)
    pilot = Pilot("Евгений", "Капитан", flight_hours=1200, health=95, energy=65)
    sci = Scientist("'Группа CS-204(c)'", "Сержант", research_field="Астрофизика", health=88, energy=60)

    station.add_crew_member(eng)
    station.add_crew_member(pilot)
    station.add_crew_member(sci)

    ship = Spacecraft("Задание 5", "Практическая работа", crew_capacity=2, hull_integrity=100)
    station.spacecraft_fleet.append(ship)

    station.assign_crew_to_ship([pilot, eng], ship)

    print("\n=== Работа экипажа ===")
    for member in [eng, pilot, sci]:
        member.work()
        print(member.status_report())

    print("\n=== Запуск миссии ===")
    ship.launch_mission("Луна")

    print("\n=== Исследование ===")
    sci.work()
    print(sci.status_report())

    print("\n=== Ежедневные операции ===")
    station.daily_operations()

    print("\n=== Итоговый отчёт ===")
    station.generate_report()
