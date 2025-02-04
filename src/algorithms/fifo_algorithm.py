from src.page import Page
from src.algorithms.base_algorithm import BaseAlgorithm

class FIFOAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas FIFO (First-In-First-Out).

    Nesse algoritmo, a página a ser substituída é aquela que está a mais tempo na memória
    
    """

    NAME = "FIFO"

    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:

                self.pages_in_memory.pop(0)
            
            self.pages_in_memory.append(current_referenced_page)
            had_page_fault = True
        
        return had_page_fault
