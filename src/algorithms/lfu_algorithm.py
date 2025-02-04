from src.page import Page
from src.replacement_algorithm.base_algorithm import BaseAlgorithm

class LFUAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas LFU (Least-Frequently-Used).

    Nesse algoritmo, a página a ser substituída é aquela que possui a menor contagem de referências
    
    """
    

    NAME = "LFU"

    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:

                less_referenced_page: Page = min(self.pages_in_memory, key=lambda x: x.reference_counter)
                less_referenced_page_index: int = self.pages_in_memory.index(less_referenced_page)

                self.pages_in_memory.pop(less_referenced_page_index)
            
            current_referenced_page.reference_counter = 1
            self.pages_in_memory.append(current_referenced_page)
            
            had_page_fault = True

        else:

            referenced_page: Page = next(filter(lambda x: x.page_id == current_referenced_page.page_id, 
                        self.pages_in_memory))
            
            referenced_page.reference_counter += 1
        
        return had_page_fault
