from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        self.capacity = 15
        super().__init__(name, self.capacity)

    def details(self):
        output = [f"{self.name} Secondary Service:",]
        if not self.robots:
            output.append("Robots: none")
        else:
            output.append(f'Robots: {" ".join([r.name for r in self.robots])}')
        return '\n'.join(output)

