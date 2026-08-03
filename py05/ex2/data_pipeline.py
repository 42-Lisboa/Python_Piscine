#! /usr/bin/env python3

from abc import ABC, abstractmethod  # ABC stands for Abstract Base Class
from typing import Any, Protocol


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


# ============================== Protocol Class ===============================
#     This class serves as a contract but doesn't need heritage to work
# -----------------------------------------------------------------------------

class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


# Class with the process_output method (Duck Typing)
class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("🟠 JSON Output:")
        print(f"🟠 {data}")


# Class with the process_output method (Duck Typing)
class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("🟣 CSV Output:")
        print(f"🟣 {data}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        pipeline_data = []
        for proc in self._proc_list:
            items_to_get = nb
            while len(proc._storage) > 0 and items_to_get > 0:
                pipeline_data.append(proc.output())
                items_to_get -= 1
        plugin.process_output(pipeline_data)


# =============================== Program Test ================================

if __name__ == "__main__":
    print(
        "\n================ 🪐 Code Nexus - Data Pipeline 🪐 ================\n"
        )

    # 1. Initialization
    # -------------------------------------------------------------------------
    print(">>> Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    # 2. Polymorphic Processor Test
    # -------------------------------------------------------------------------
    print("🧮 Registering Processors...")
    num_pro = NumericProcessor()
    txt_pro = TextProcessor()
    log_pro = LogProcessor()
    stream.register_processor(num_pro)
    stream.register_processor(txt_pro)
    stream.register_processor(log_pro)
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

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE', 'log_message': 'Certificate in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\n>>> Send another batch of data:\n{batch2}\n")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    # 3. Sending processed data to JSON plugin
    # -------------------------------------------------------------------------
    json_plugin = JSONExportPlugin()
    nb1 = 5
    print(f"\n>>> Send {nb1} "
          "processed data from each processor to a JSON plugin:")
    stream.output_pipeline(nb1, json_plugin)
    stream.print_processors_stats()

    # 4. Sending processed data to CSV plugin
    # -------------------------------------------------------------------------
    csv_plugin = CSVExportPlugin()
    nb2 = 5
    print(f"\n>>> Send {nb2} "
          "processed data from each processor to a CSV plugin:")
    stream.output_pipeline(nb2, csv_plugin)
    stream.print_processors_stats()


"""
===============================================================================
         Abstract Base Class (ABC) vs Protocol Class (typing.Protocol)
===============================================================================

1. TIPAGEM & HERANÇA:
   - ABC (Tipagem Nominal): Exige declaração de herança explícita na classe
     (ex: class MyProcessor(BaseProcessor):).
   - Protocol (Tipagem Estrutural): Não exige herança. Aplica o princípio de
     Duck Typing ("se possui os métodos e assinaturas corretas, satisfaz o
     protocolo").

2. REUTILIZAÇÃO DE CÓDIGO:
   - ABC: Permite definir métodos concretos/partilhados na classe base para
     evitar duplicação de lógica entre subclasses.
   - Protocol: Foca estritamente na assinatura dos métodos (contrato de
     comportamento), sem partilha de código ou implementação.

3. MOMENTO DE VALIDAÇÃO:
   - ABC: Valida obrigatoriamente em TEMPO DE EXECUÇÃO (Runtime). Impede a
     instanciação de classes com métodos abstratos pendentes.
   - Protocol: Valida primariamente em TEMPO DE ANÁLISE ESTÁTICA através de
     ferramentas de linters e typers (ex: mypy).

-------------------------------------------------------------------------------
QUANDO USAR CADA UMA NO PIPELINE:
-------------------------------------------------------------------------------
- Use Abstract Base Class (ABC) quando:
  * Controlar toda a hierarquia do sistema e quiser partilhar código comum.
  * Precisar de bloquear a instanciação de classes incompletas em tempo de
  execução.

- Use Protocol quando:
  * Quiser aplicar Duck Typing com segurança de verificação de tipos estáticos.
  * Precisar de criar sistemas de plugins flexíveis ou integrar bibliotecas de
    terceiros sem alterar o código original das mesmas.
===============================================================================
"""
