import heapq

# 어떻게 최신인지를 관리할까? -> 최신인 정보를 미리 캐싱해두면 되는거였음
# class StockPrice:

#     def __init__(self):
#         self.min_pq = []
#         self.max_pq = []
#         self.last_timestamp = 0
#         self.last_price = 0
        
#     def update(self, timestamp: int, price: int) -> None:
#         if self.last_timestamp <= timestamp:
#             self.last_timestamp = timestamp
#             self.last_price = price
        
#         if self.min_pq and self.min_pq[0][1] == timestamp:
#             heapq.heappop(self.min_pq)
#         heapq.heappush(self.min_pq, [price, timestamp])
        
#         if self.max_pq and self.max_pq[0][1] == timestamp:
#             heapq.heappop(self.max_pq)
#         heapq.heappush(self.max_pq, [-price, timestamp])

#     def current(self) -> int:
#         return self.last_price

#     def maximum(self) -> int:
#         return -self.max_pq[0][0]

#     def minimum(self) -> int:
#         return self.min_pq[0][0]

# 수정 7분가량
class StockPrice:

    def __init__(self):
        self.min_pq = []
        self.max_pq = []
        self.last_timestamp = 0
        self.last_price = 0
        self.timestamp_price = {}
        
    def update(self, timestamp: int, price: int) -> None:
        if self.last_timestamp <= timestamp:
            self.last_timestamp = timestamp
            self.last_price = price
        self.timestamp_price[timestamp] = price
        
        heapq.heappush(self.min_pq, [price, timestamp])
        heapq.heappush(self.max_pq, [-price, timestamp])

    def current(self) -> int:
        return self.last_price

    def maximum(self) -> int:
        while self.max_pq and self.timestamp_price[self.max_pq[0][1]] != -self.max_pq[0][0]:
            heapq.heappop(self.max_pq)
        return -self.max_pq[0][0]

    def minimum(self) -> int:
        while self.min_pq and self.timestamp_price[self.min_pq[0][1]] != self.min_pq[0][0]:
            heapq.heappop(self.min_pq)
        return self.min_pq[0][0]

