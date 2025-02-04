from typing import List


from src.page import Page

class BaseAlgorithm:

    """Classe base para os algoritmos de substituição
    """

    def __init__(self, pages_references: List[int], frames_amount: int) -> None:

        """Inicializa um algoritmo de substituição de página

        Parameters
        ----------
        pages_references : List[int]
            Uma lista com os ids das páginas referenciadas

        frames_amount : int
            Quantidade de frames (páginas em memória)
        """

        self.pages_references = list(map(lambda x: Page(x), pages_references))
        self._pages_references_copy = self.pages_references.copy()

        self.frames_amount = frames_amount

        self.pages_in_memory = []
    
    def countPageFault(self) -> int:

        """Conta a quantidade de page fault causada pelas referências às páginas

        Returns
        -------
        int
            Quantidade de page fault causada pelas referências às páginas
        """

        page_fault_counter = 0

        # Reinicio dos valores dos atributos
        self.pages_references = self._pages_references_copy.copy()
        self.pages_in_memory = []

        while self.pages_references:

            had_page_fault = self.executeReference()

            if had_page_fault:

                page_fault_counter += 1
        
        self.pages_references = self._pages_references_copy.copy()
        self.pages_in_memory = []
        
        return page_fault_counter

    def executeReference(self) -> bool:

        """Executa uma única referência da lista de referências às páginas

        Returns
        -------
        bool
            Se True, a referência à página em questão ocasionou um page fault
        
        """

        pass

        
    