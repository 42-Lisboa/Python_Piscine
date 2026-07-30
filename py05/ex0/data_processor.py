#! /usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._storage = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if (type(data) is int) or (type(data) is float):
            return True
        elif type(data) is list:
            for value in data:
                if (type(value) is not int) and (type(value) is not float):
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise TypeError("❌ Invalid data: data is not numeric")
        if type(data) is not list:
            data = [data]
        for i in data:
            self._rank += 1
            self._storage.append((self._rank - 1, str(i)))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        elif type(data) is list:
            for value in data:
                if type(value) is not str:
                    return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise TypeError("❌ Invalid data: data is not text")
        if type(data) is not list:
            data = [data]
        for i in data:
            self._rank += 1
            self._storage.append((self._rank - 1, str(i)))


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if type(data) is dict:
            for k, v in data.items():
                if (type(k) is not str) or (type(v) is not str):
                    return False
            return True
        elif type(data) is list:
            for value in data:
                if type(value) is not dict:
                    return False
                for k, v in value.items():
                    if (type(k) is not str) or (type(v) is not str):
                        return False
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data) is False:
            raise TypeError("❌ Invalid data: data is not log")
        if type(data) is not list:
            data = [data]
        for i in data:
            self._rank += 1
            # the current dict will always have only two items
            i = ": ".join(i.values())
            self._storage.append((self._rank - 1, i))
