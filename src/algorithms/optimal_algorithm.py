from src.page import Page
from src.algorithms.base_algorithm import BaseAlgorithm

class OptimalAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas Ótimo.

    Nesse algoritmo, a página a ser substituída é aquela que não será mais referenciada ou com maior intervalo de tempo para ser referenciada
    
    """
    

    NAME = "Optimal"

    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:

                pages_references_ids = list(map(lambda x: x.page_id, self.pages_references))
                selected_page_index: int = -1

                # Verifica se as páginas em memória não serão mais referenciadas
                for i in range(len(self.pages_in_memory)):

                    if pages_references_ids.count(self.pages_in_memory[i].page_id) == 0:

                        selected_page_index = i
                        break
                
                # Caso todas sejam referenciadas no futuro, verifica qual irá demorar mais para ser
                # referenciada
                if selected_page_index == -1:

                    higher_index: int = -1

                    for i in range(len(self.pages_references)):

                        for j in range(len(self.pages_in_memory)):

                            context_page_reference_id: int = pages_references_ids[i]
                            context_frame: Page = self.pages_in_memory[j]


                            if (context_frame.page_id == context_page_reference_id) and (i > higher_index):

                                higher_index = i
                                selected_page_index = j

                self.pages_in_memory.pop(selected_page_index)
            
            self.pages_in_memory.append(current_referenced_page)
            
            had_page_fault = True
        
        return had_page_fault
