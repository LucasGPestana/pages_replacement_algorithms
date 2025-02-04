from src.page import Page
from src.replacement_algorithm.base_algorithm import BaseAlgorithm

class LRUAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas LRU (Least-Recently-Used).

    Nesse algoritmo, a página a ser substituída é aquela que foi referenciada a mais tempo
    
    """
    

    NAME = "LRU"

    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:

                more_time_referenced_page: Page = max(self.pages_in_memory, key=lambda x: x.reference_time)
                more_time_referenced_page_index: int = self.pages_in_memory.index(more_time_referenced_page)

                self.pages_in_memory.pop(more_time_referenced_page_index)
            
            current_referenced_page.reference_time = 0
            self.pages_in_memory.append(current_referenced_page)
            
            had_page_fault = True

        else:

            referenced_page: Page = next(filter(lambda x: x.page_id == current_referenced_page.page_id, 
                        self.pages_in_memory))
            
            referenced_page.reference_time = 0
        
        for page in self.pages_in_memory:
            
            page.reference_time += 1
        
        return had_page_fault
