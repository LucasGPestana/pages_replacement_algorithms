class Page:

    def __init__(self, page_id: int) -> None:

        self.page_id = page_id
        self.reference_time = 0
        self.bit_reference = 0
        self.reference_counter = 0
    
    def __str__(self) -> str:

        return f"Page {self.page_id}"
    
    def __repr__(self) -> str:
        
        return f"Page {self.page_id}"