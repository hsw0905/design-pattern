from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        ...

    @abstractmethod
    def produce_part_a(self) -> None:
        ...

    @abstractmethod
    def produce_part_b(self) -> None:
        ...

    @abstractmethod
    def produce_part_c(self) -> None:
        ...
