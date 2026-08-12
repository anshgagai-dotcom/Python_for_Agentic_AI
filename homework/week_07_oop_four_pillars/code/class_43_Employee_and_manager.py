"""
Create an Employee parent class with name and salary. 
Create a Manager child class that uses super() to initialize the parent attributes and adds a team_size attribute.
"""
# Employee parent (name, salary); Manager child jo super() use kare aur ek team_size add kare.



class Employee:
    """
    Represent an employee.
    """

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialize an employee with name and salary.
        """
        self.name = name
        self.salary = salary


class Manager(Employee):
    """
    Represent a manager who manages a team.
    """

    def __init__(
        self,
        name: str,
        salary: float,
        team_size: int
    ) -> None:
        """
        Initialize a manager with employee and team details.
        """
        super().__init__(name, salary)
        self.team_size = team_size


manager = Manager("Asha", 90000, 5)

print(manager.name)
print(manager.salary)
print(manager.team_size)