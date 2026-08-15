from abc import ABC, abstractmethod


class Tool(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args):
        ...


class CalculatorTool(Tool):

    def __init__(self):
        super().__init__(
            "Calculator",
            "A tool for adding and multiplying numbers"
        )

    def add(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def run(self, *args):
        a, b, name = args

        if name == "add":
            return self.add(a, b)

        elif name == "mul":
            return self.multiplication(a, b)

        else:
            raise ValueError(f"Invalid operation: {name}")


class GreeterTool(Tool):

    def __init__(self):
        super().__init__(
            "greeter",
            "A tool for greeting"
        )

    def run(self, *args):
        name = args[0]
        return f"Hello, {name}!"


class Agent:

    def __init__(self, name):
        self.name = name
        self.tools = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def list_tool(self):
        for tool in self.tools:
            print(f"{tool.name}, {tool.description}")

    def use_tool(self, tool_name: str, *args):
        for tool in self.tools:

            if tool.name.lower() == tool_name.lower():
                return tool.run(*args)

        return f"Tool {tool_name} not found"


agent = Agent("My first agent")


agent.add_tool(CalculatorTool())
agent.add_tool(GreeterTool())


agent.list_tool()


add_result = agent.use_tool("calculator", 5, 7, "add")
mul_result = agent.use_tool("calculator", 5, 7, "mul")


greet_result = agent.use_tool("greeter", "Ansh")


print("Addition result:", add_result)
print("Multiplication result:", mul_result)
print("Greeting result:", greet_result)


