from src.page import Page
from src.algorithms.base_algorithm import BaseAlgorithm


import random


class RandomAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas Aleatório.

    Nesse algoritmo, todas as páginas em memória possuem a mesma chance de serem substituidas.
    
    """

    NAME = "Random"

    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:

                selected_page_index = random.randint(0, len(self.pages_in_memory) - 1)

                self.pages_in_memory.pop(selected_page_index)
            
            self.pages_in_memory.append(current_referenced_page)
            had_page_fault = True
        
        return had_page_fault
