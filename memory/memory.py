from typing import List


class Memory:
    """
    Memory module for storing and retrieving agent interactions.
    """

    def __init__(self):
        self.history: List[str] = []

    def add(self, entry: str) -> None:
        """
        Store an entry in memory.
        """
        self.history.append(entry)

    def get_all(self) -> List[str]:
        """
        Retrieve all stored memory entries.
        """
        return self.history
