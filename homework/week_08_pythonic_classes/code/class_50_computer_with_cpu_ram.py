
# Computer class banao jo CPU aur RAM objects rakhe. This is called composition.
# Create a Computer class that contains CPU and RAM objects. This relationship is called composition.




class CPU:
    """
    Represent a computer CPU.
    """
    def __init__(self, cores: int) -> None:
        """
        Initialize the CPU with a number of cores.
        """
        self.cores = cores


class RAM:
    """
    Represent computer RAM.
    """
    def __init__(self, size: int) -> None:
        """
        Initialize RAM with a size in GB.
        """
        self.size = size


class Computer:
    """
    Represent a computer made from CPU and RAM components.
    """
    def __init__(self) -> None:
        """
        Create a computer with a CPU and RAM
        ."""
        self.cpu = CPU(6)
        self.ram = RAM(32)


computer = Computer()

print(computer.cpu.cores)
print(computer.ram.size)

