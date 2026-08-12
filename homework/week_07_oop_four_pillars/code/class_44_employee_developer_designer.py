"""
Create an Employee parent class with a work() method. 
Create Developer and Designer child classes that override work() with different behavior.
"""
# Employee parent with work(); Developer aur Designer children jo alag-alag work print karein.




class Employee:
    """
    Represent a general employee.
    """

    def work(self) -> str:
        """
        Return the employee's work description.
        """
        return "Employee is working"


class Developer(Employee):
    """
    Represent a software developer.
    """

    def work(self) -> str:
        """
        Return the developer's work description.
        """
        return "Developer is writing Python code"


class Designer(Employee):
    """Represent a UI designer."""

    def work(self) -> str:
        """
        Return the designer's work description.
        """
        return "Designer is creating UI designs"


employees: list[Employee] = [Developer(),Designer()]

for employee in employees:
    print(employee.work())