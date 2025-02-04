from typing import List


from src.page import Page
from src.algorithms.base_algorithm import BaseAlgorithm

class ClockAlgorithm(BaseAlgorithm):

    """Representa o algoritmo de substituição de páginas Clock (FIFO Circular).

    Nesse algoritmo, a página a ser substituída é aquela que possui bit de referência 0.

    Regras:

        - Usa-se um ponteiro para apontar para a posição da página cujo bit de referência será verificado;
        - Se a página apontada possuir bit de referência 1, ele será setado para 0 e o ponteiro incrementado;
        - Caso o ponteiro percorra toda a memória, ele apontará para a primeira página (mais antiga), e ela será removida;
        - Toda página carregada em memória começa com bit de referência 0
    
    """

    NAME = "Clock"

    def __init__(self, pages_references: List[int], frames_amount: int) -> None:

        super().__init__(pages_references, frames_amount)
        self.pointer = 0


    def executeReference(self) -> bool:

        current_referenced_page: Page = self.pages_references.pop(0)
        had_page_fault = False

        pages_in_memory_ids = list(map(lambda x: x.page_id, 
                                       self.pages_in_memory))

        if not current_referenced_page.page_id in pages_in_memory_ids:

            # Memória cheia
            if len(self.pages_in_memory) == self.frames_amount:


                # Busca uma página para substituir
                while self.pages_in_memory[self.pointer].bit_reference == 1:

                    self.pages_in_memory[self.pointer].bit_reference = 0

                    self.pointer += 1

                    # Garante que o ponteiro volte ao início da lista (circularidade)
                    if self.pointer >= len(self.pages_in_memory):

                        self.pointer = 0
                        break
                
                self.pages_in_memory.pop(self.pointer)

            self.pages_in_memory.append(current_referenced_page)
            had_page_fault = True
        
        else:

            # Situação em que uma página já em memória foi referenciada

            referenced_page = next(filter(lambda x: x.page_id == current_referenced_page.page_id, 
                   self.pages_in_memory))
            
            referenced_page.bit_reference = 1
        
        return had_page_fault
