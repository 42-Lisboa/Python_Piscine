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


# ============================= DataStream Class ==============================
#     Serves as a streamline for various types of entries for the processors
# -----------------------------------------------------------------------------

class DataStream():
    def __init__(self):
        self._proc_list = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for proc in self._proc_list:
                if proc.validate(data) is True:
                    proc.ingest(data)
                    break
            else:
                print(f"❌ DataStream error - "
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("\n==== 📊  DataStream Statistics 📊 ====")
        if self._proc_list == []:
            print("⚠️  No processor found, no data!\n")
        for proc in self._proc_list:
            proc_name = type(proc).__name__  # .__name__ show only the name
            proc_total = proc._rank
            proc_remain = len(proc._storage)
            print(f">>> {proc_name}: total {proc_total} items processed, "
                  f"remaining {proc_remain} on processor")


# =============================== Program Test ================================

if __name__ == "__main__":
    print(
        "\n================= 🪐 Code Nexus - Data Stream 🪐 =================\n"
        )

    # 1. Initialization
    # -------------------------------------------------------------------------
    print(">>> Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    # 2. Single Processor Test (Numeric)
    # -------------------------------------------------------------------------
    print("🧮 Registering Numeric Processor...")
    num_pro = NumericProcessor()
    stream.register_processor(num_pro)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Error access! Use ssh'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f">>> Send first batch of data on stream:\n{batch}\n")
    stream.process_stream(batch)
    stream.print_processors_stats()

    # 3. Full Polymorphic Test
    # -------------------------------------------------------------------------
    print("\n📦 Registering other data processors (Text and Log)...")
    txt_pro = TextProcessor()
    log_pro = LogProcessor()
    stream.register_processor(txt_pro)
    stream.register_processor(log_pro)

    print(">>> Send the same batch again:")
    stream.process_stream(batch)
    stream.print_processors_stats()

    # 4. Output/Consumption Test
    # -------------------------------------------------------------------------
    print("\n🍽️  Consume some elements from the data processors: "
          "3 Numeric, 2 Text, 1 Log")
    for _ in range(3):  # Consuming 3 elements from Numeric Processor
        num_pro.output()
    for _ in range(2):  # Consuming 2 elements from Text Processor
        txt_pro.output()
    for _ in range(1):  # Consuming 1 element from Log Processor
        log_pro.output()

    stream.print_processors_stats()
    print("--------------------------------------------------------------")
    print(f">>> Remains on NumericProcessor storage: {num_pro._storage}")
    print(f">>> Remains on TextProcessor storage: {txt_pro._storage}")
    print(f">>> Remains on LogProcessor storage: {log_pro._storage}")
    print("\n==============================================================\n")
