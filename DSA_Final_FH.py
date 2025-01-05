import matplotlib.pyplot as plt
import networkx as nx

# Graph Class
traffic_network = nx.DiGraph()

# Initialize the traffic network with some predefined intersections and roads
def initialize_traffic_network():
    global traffic_network
    traffic_network.add_node("Intersection A")
    traffic_network.add_node("Intersection B")
    traffic_network.add_node("Intersection C")
    traffic_network.add_node("Intersection D")
    traffic_network.add_edge("Intersection A", "Intersection B", weight=5)
    traffic_network.add_edge("Intersection B", "Intersection C", weight=3)
    traffic_network.add_edge("Intersection C", "Intersection D", weight=2)
    traffic_network.add_edge("Intersection A", "Intersection D", weight=10)

# Display the traffic network
def display_traffic_network():
    pos = nx.spring_layout(traffic_network)
    labels = nx.get_edge_attributes(traffic_network, 'weight')
    nx.draw(traffic_network, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(traffic_network, pos, edge_labels=labels)
    plt.show()

# Detect traffic bottlenecks (cycles)
def detect_bottlenecks():
    try:
        cycles = list(nx.find_cycle(traffic_network, orientation='original'))
        if cycles:
            print("Traffic bottleneck detected at:", cycles)
    except nx.NetworkXNoCycle:
        print("No traffic bottlenecks detected in the network.")

# Suggest optimal traffic routes (Topological Sort)
def suggest_optimal_routes():
    try:
        order = list(nx.topological_sort(traffic_network))
        print("Suggested Optimal Traffic Flow Order:", order)
    except nx.NetworkXUnfeasible:
        print("Traffic network is not suitable for optimal flow suggestions (contains bottlenecks).")

# Stack Implementation
class VehicleStack:
    def __init__(self):
        self.stack = []

    def add_vehicle(self, vehicle):
        self.stack.append(vehicle)
        print(f"Vehicle {vehicle} added to the stack.")

    def remove_vehicle(self):
        if self.stack:
            vehicle = self.stack.pop()
            print(f"Vehicle {vehicle} removed from the stack.")
        else:
            print("No vehicles in the stack.")

# Queue Implementation
class TrafficQueue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, vehicle):
        self.queue.append(vehicle)
        print(f"Vehicle {vehicle} added to the traffic queue.")

    def pass_vehicle(self):
        if self.queue:
            vehicle = self.queue.pop(0)
            print(f"Vehicle {vehicle} passed through the traffic queue.")
        else:
            print("No vehicles in the traffic queue.")

# Sorting Algorithms
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if x <= pivot]
    greater = [x for x in data[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def heap_sort(data):
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left

    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

# Search Algorithms
def binary_search(data, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Main Menu
def main_menu():
    vehicle_stack = VehicleStack()
    traffic_queue = TrafficQueue()
    initialize_traffic_network()

    while True:
        print("\nTraffic Management System")
        print("1. Show Traffic Network")
        print("2. Add Intersection")
        print("3. Add Road")
        print("4. Detect Traffic Bottlenecks")
        print("5. Suggest Optimal Traffic Routes")
        print("6. Manage Vehicles at Intersection (Stack)")
        print("7. Manage Traffic Queue")
        print("8. Sort Traffic Data")
        print("9. Search Traffic Data")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_traffic_network()
        elif choice == "2":
            intersection = input("Enter intersection name: ")
            traffic_network.add_node(intersection)
            print(f"Intersection {intersection} added.")
        elif choice == "3":
            start = input("Enter starting intersection: ")
            end = input("Enter ending intersection: ")
            weight = int(input("Enter road weight (e.g., distance or time): "))
            traffic_network.add_edge(start, end, weight=weight)
            print(f"Road from {start} to {end} with weight {weight} added.")
        elif choice == "4":
            detect_bottlenecks()
        elif choice == "5":
            suggest_optimal_routes()
        elif choice == "6":
            print("Vehicle Stack Operations")
            print("1. Add Vehicle")
            print("2. Remove Vehicle")
            stack_choice = input("Enter your choice: ")
            if stack_choice == "1":
                vehicle = input("Enter vehicle name or ID: ")
                vehicle_stack.add_vehicle(vehicle)
            elif stack_choice == "2":
                vehicle_stack.remove_vehicle()
        elif choice == "7":
            print("Traffic Queue Operations")
            print("1. Add Vehicle to Queue")
            print("2. Pass Vehicle from Queue")
            queue_choice = input("Enter your choice: ")
            if queue_choice == "1":
                vehicle = input("Enter vehicle name or ID: ")
                traffic_queue.add_to_queue(vehicle)
            elif queue_choice == "2":
                traffic_queue.pass_vehicle()
        elif choice == "8":
            data = list(map(int, input("Enter traffic data (e.g., speeds or times) separated by space: ").split()))
            print("Sorting Methods")
            print("1. Merge Sort")
            print("2. Quick Sort")
            print("3. Heap Sort")
            sort_choice = input("Enter your choice: ")
            if sort_choice == "1":
                merge_sort(data)
                print("Sorted Data:", data)
            elif sort_choice == "2":
                data = quick_sort(data)
                print("Sorted Data:", data)
            elif sort_choice == "3":
                heap_sort(data)
                print("Sorted Data:", data)
        elif choice == "9":
            data = list(map(int, input("Enter traffic data (e.g., speeds or times) separated by space: ").split()))
            target = int(input("Enter data point to search for: "))
            print("Search Methods")
            print("1. Linear Search")
            print("2. Binary Search")
            search_choice = input("Enter your choice: ")
            if search_choice == "1":
                result = linear_search(data, target)
                if result != -1:
                    print(f"Data point {target} found at index {result}.")
                else:
                    print(f"Data point {target} not found.")
            elif search_choice == "2":
                data.sort()  # Binary search requires sorted data
                result = binary_search(data, target)
                if result != -1:
                    print(f"Data point {target} found at index {result}.")
                else:
                    print(f"Data point {target} not found.")
        elif choice == "10":
            print("Exiting Traffic Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()