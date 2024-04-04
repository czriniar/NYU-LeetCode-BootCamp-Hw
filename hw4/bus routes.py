class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Create a stop_to_routes map to store which routes go through each stop
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        # Initialize a set to keep track of visited buses
        visited = set()
        
        # Initialize the queue for BFS
        queue = deque([(source, 0)])
        
        while queue:
            curr_stop, num_buses = queue.popleft()
            
            if curr_stop == target:
                return num_buses
            
            for bus in stop_to_routes[curr_stop]:
                if bus not in visited:
                    visited.add(bus)
                    for next_stop in routes[bus]:
                        queue.append((next_stop, num_buses + 1))
        
        return -1  # If target is not reachable
