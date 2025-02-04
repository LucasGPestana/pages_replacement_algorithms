from src.algorithms.fifo_algorithm import FIFOAlgorithm
from src.algorithms.clock_algorithm import ClockAlgorithm
from src.algorithms.lfu_algorithm import LFUAlgorithm
from src.algorithms.lru_algorithm import LRUAlgorithm
from src.algorithms.optimal_algorithm import OptimalAlgorithm
from src.algorithms.random_algorithm import RandomAlgorithm


from src.utils.results import getResultsFromAlgorithm

pages_references = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2, 3, 1, 4, 5, 6]

fifo = FIFOAlgorithm(pages_references, 3)

clock = ClockAlgorithm(pages_references, 3)

lfu = LFUAlgorithm(pages_references, 3)

lru = LRUAlgorithm(pages_references, 3)

optimal = OptimalAlgorithm(pages_references, 3)

random = RandomAlgorithm(pages_references, 3)

for algorithm in (fifo, clock, lfu, lru, optimal, random):

    getResultsFromAlgorithm(algorithm)