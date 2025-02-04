from src.algorithms.base_algorithm import BaseAlgorithm
from src.algorithms.clock_algorithm import ClockAlgorithm


import os


def getResultsFromAlgorithm(algorithm: BaseAlgorithm) -> None:

    FILENAME = f"{algorithm.NAME.lower()}_results.txt"
    PROJECT_DIRPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    FILEPATH = os.path.join(PROJECT_DIRPATH, "files", FILENAME)

    file_stream_man = open(FILEPATH, 'w', encoding="utf-8")

    stream_lines = []

    while algorithm.pages_references:

        had_page_fault = algorithm.executeReference()

        pages_in_memory = algorithm.pages_in_memory

        if isinstance(algorithm, ClockAlgorithm):

            pages_in_memory = list(zip(algorithm.pages_in_memory, 
                                       map(lambda x: x.bit_reference, algorithm.pages_in_memory)))
    
        stream_lines.extend([
            f"{'---'*30}\n", 
            f"Páginas em memória: {pages_in_memory}\n", 
            f"Teve Page Fault? {'Sim' if had_page_fault else 'Não'}\n", 
            f"{'---'*30}\n"
            ])

    stream_lines.append(f"\nNúmero de Page Fault: {algorithm.countPageFault()}")

    file_stream_man.writelines(stream_lines)
    file_stream_man.close()

    print(f"Caminho do arquivo: {FILEPATH}")

