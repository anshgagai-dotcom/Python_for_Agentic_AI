# Upar wale Agent project mein ek teesra tool add karo: ReverseTool jo string ko ulta kare.
# Add a third tool called ReverseTool to the Agent project. It should reverse a given string.



from abc import ABC, abstractmethod


class Tool(ABC):
    """
    Base class for all tools.
    """

    def __init__(self, name: str, description: str) -> None:
        """
        Initialize a tool with a name and description.
        """
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args: object) -> object:
        """
        Execute the tool.
        """
        ...


class CalculatorTool(Tool):
    """
    A tool for adding and multiplying numbers.
    """

    def __init__(self) -> None:
        """
        Initialize the calculator tool.
        """
        super().__init__("Calculator","A tool for adding and multiplying numbers")

    def add(self, a: int, b: int) -> int:
        """
        Return the sum of two numbers.
        """
        return a + b

    def multiplication(self, a: int, b: int) -> int:
        """
        Return the multiplication of two numbers.
        """
        return a * b

    def run(self, *args: object) -> int:
        """
        Perform the requested calculator operation.
        """

        a, b, name = args

        if name == "add":
            return self.add(a, b)

        elif name == "mul":
            return self.multiplication(a, b)

        else:
            raise ValueError(f"Invalid operation: {name}")


class GreeterTool(Tool):
    """
    A tool for greeting users.
    """

    def __init__(self) -> None:
        """
        Initialize the greeter tool.
        """
        super().__init__("greeter","A tool for greeting")

    def run(self, *args: object) -> str:
        """
        Return a greeting message.
        """

        name = args[0]

        return f"Hello, {name}!"


class ReverseTool(Tool):
    """
    A tool that reverses a string.
    """

    def __init__(self) -> None:
        """
        Initialize the reverse tool.
        """
        super().__init__("reverse","Reverses a string")

    def run(self, text: str) -> str:
        """
        Return the given text in reverse order.
        """
        return text[::-1]


class Agent:
    """
    An agent that can manage and use multiple tools.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the agent.
        """
        self.name = name
        self.tools: list[Tool] = []

    def add_tool(self, tool: Tool) -> None:
        """
        Add a tool to the agent.
        """
        self.tools.append(tool)

    def list_tool(self) -> None:
        """
        Display all tools available to the agent.
        """

        for tool in self.tools:
            print(f"{tool.name}, {tool.description}")

    def use_tool(self, tool_name: str, *args: object) -> object:
        """
        Find and execute a tool by its name.
        """

        for tool in self.tools:

            if tool.name.lower() == tool_name.lower():
                return tool.run(*args)

        return f"Tool {tool_name} not found"


agent = Agent("My first agent")

agent.add_tool(CalculatorTool())
agent.add_tool(GreeterTool())
agent.add_tool(ReverseTool())


print("Available Tools:")
agent.list_tool()


add_result = agent.use_tool("calculator",5,7,"add")

mul_result = agent.use_tool("calculator",5,7,"mul")


greet_result = agent.use_tool("greeter","Ansh")


reverse_result = agent.use_tool("reverse","hello")


print("\nResults:")

print("Addition result:", add_result)
print("Multiplication result:", mul_result)
print("Greeting result:", greet_result)
print("Reverse result:", reverse_result)











        