#! /usr/bin/env python3

from abc import ABC, abstractmethod  # ABC stands for Abstract Base Class
from typing import Any


# ============================== Abstract Class ===============================
#   Abstract class is like a contract with the major skeleton for sub classes
# -----------------------------------------------------------------------------

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


# ============================= Concrete Classes ==============================
#         Concrete classes unlike the abstract ones can be instanciated
# -----------------------------------------------------------------------------

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


# ============================== Program Test ================================

if __name__ == "__main__":
    print("\n============== 🪐 Code Nexus - Data Processor 🪐 ==============\n")

    # Instatiate objects
    num_pro = NumericProcessor()
    txt_pro = TextProcessor()
    log_pro = LogProcessor()

    # Testing Numeric Processor
    # --------------------------------------------------------------------------

    print("🧮 Testing Numeric Processor...")

    # Validation Method
    print(">>> Test validation method:")
    num_in1 = 42
    print(f"Validate single input '{num_in1}': ✅ {num_pro.validate(num_in1)}")
    num_in2 = "Hello"
    print(f"Validate single input '{num_in2}': ❌ {num_pro.validate(num_in2)}")
    num_in3 = [42, 4.35]
    print(f"Validate list input '{num_in3}': ✅ {num_pro.validate(num_in3)}")
    num_in4 = [42, "Hello"]
    print(f"Validate list input '{num_in4}': ❌ {num_pro.validate(num_in4)}")

    # Invalid Ingestion
    num_in5 = "foo"
    print(f"\n>>> Test invalid ingestion of string '{num_in5}' "
          f"without prior validation:")
    try:
        num_pro.ingest(num_in5)
        print(f"Processing data: ✅ {num_in5}")
    except Exception as e:
        print(f"Got exception: {e}\n")

    # Valid Ingestion
    print(">>> Test valid ingestion and output method:")
    num_in6 = [1, 2, 3, 4, 5]
    num_pro.ingest(num_in6)
    print(f"Processing data: ✅ {num_in6}")

    # Output Method
    extract = 3
    print(f"Extracting {extract} value(s)...")
    while extract > 0:
        value = num_pro.output()
        print(f"Numeric value {value[0]}: {value[1]}")
        extract -= 1

    # Testing Text Processor
    # --------------------------------------------------------------------------

    print("\n🔤 Testing Text Processor...")

    # Validation Method
    print(">>> Test validation method:")
    txt_in1 = "Hello"
    print(f"Validate single input '{txt_in1}': ✅ {txt_pro.validate(txt_in1)}")
    txt_in2 = 42
    print(f"Validate single input '{txt_in2}': ❌ {txt_pro.validate(txt_in2)}")
    txt_in3 = ["Hello", "World"]
    print(f"Validate list input '{txt_in3}': ✅ {txt_pro.validate(txt_in3)}")
    txt_in4 = [42, "Hello"]
    print(f"Validate list input '{txt_in4}': ❌ {txt_pro.validate(txt_in4)}")

    # Invalid Ingestion
    txt_in5 = 42
    print(f"\n>>> Test invalid ingestion of string '{txt_in5}' "
          f"without prior validation:")
    try:
        txt_pro.ingest(txt_in5)
        print(f"Processing data: ✅ {txt_in5}")
    except Exception as e:
        print(f"Got exception: {e}\n")

    # Valid Ingestion
    print(">>> Test valid ingestion and output method:")
    txt_in6 = ['Hello', 'Nexus', 'World']
    txt_pro.ingest(txt_in6)
    print(f"Processing data: ✅ {txt_in6}")

    # Output Method
    extract = 2
    print(f"Extracting {extract} value(s)...")
    while extract > 0:
        value = txt_pro.output()
        print(f"Text value {value[0]}: {value[1]}")
        extract -= 1

    # Testing Log Processor
    # --------------------------------------------------------------------------

    print("\n📦 Testing Log Processor...")

    # Validation Method
    print(">>> Test validation method:")
    log_in1 = {"Hello": "hey", "Good": "hi"}
    print(f"Validate single input '{log_in1}': ✅ {log_pro.validate(log_in1)}")
    log_in2 = "Hello"
    print(f"Validate single input '{log_in2}': ❌ {log_pro.validate(log_in2)}")
    log_in3 = [{"Ana": 'A', "João": 'B'}, {"Ceu": 'A', "Ro": 'D'}, {"Lu": 'B'}]
    print(f"Validate list input '{log_in3}': ✅ {log_pro.validate(log_in3)}")
    log_in4 = [{"Ana": 'A', "João": 'B'}, "Hello"]
    print(f"Validate list input '{log_in4}': ❌ {log_pro.validate(log_in4)}")

    # Invalid Ingestion
    log_in5 = 42
    print(f"\n>>> Test invalid ingestion of string '{log_in5}' "
          f"without prior validation:")
    try:
        log_pro.ingest(log_in5)
        print(f"Processing data: ✅ {log_in5}")
    except Exception as e:
        print(f"Got exception: {e}\n")

    # Valid Ingestion
    print(">>> Test valid ingestion and output method:")
    log_in6 = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
               {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
               {'log_level': 'PAUSE', 'log_message': 'Temporarily offline!!'}]
    log_pro.ingest(log_in6)
    print(f"Processing data: ✅ {log_in6}")

    # Output Method
    extract = 2
    print(f"Extracting {extract} value(s)...")
    while extract > 0:
        value = log_pro.output()
        print(f"Log entry {value[0]}: {value[1]}")
        extract -= 1
