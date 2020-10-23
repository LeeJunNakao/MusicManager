from typing import Protocol


class Writer(Protocol):
    def capsLock(self, content: str) -> str:
        ...

    def print(self, content: str) -> None:
        ...


class Shakespeare:
    def capsLock(self, content: str) -> str:
        return content.upper()

    def print(self, content: str) -> None:
        print(content)


class Person:
    def print(self, writer: Writer, content) -> None:
        writer.print(content)


person = Person()
person.print(Shakespeare(), "Testando")
