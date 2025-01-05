# **FH_DSA_Final**

## **Usage**
### _Run the Program_
After running the program, you'll be presented with a menu of options. Select any option by entering its corresponding number.

### _Features in Detail_
1. **Show Traffic Network**  
   Visualizes the network as a graph with intersections (nodes) and roads (edges).  
   **Example:**  
   - Input: `1` (to show the network).
   - Output: A list or graphical representation of intersections and roads with weights.

2. **Add Intersection**  
   Allows you to add a new intersection to the network.  
   **Example:**  
   - Input: `2`
   - Enter Intersection Name: `A`

3. **Add Road**  
   Adds a road between two intersections and sets its weight (distance or travel time).  
   **Example:**  
   - Input: `3`
   - Enter Intersection 1: `A`
   - Enter Intersection 2: `B`
   - Enter Weight: `5`

4. **Detect Traffic Bottlenecks**  
   Identifies bottlenecks or cycles in the network.  
   **Example:**  
   - Input: `4`
   - Output: List of bottlenecks or "No bottlenecks detected."

5. **Suggest Optimal Traffic Routes**  
   Finds the shortest route between two intersections.  
   **Example:**  
   - Input: `5`
   - Enter Starting Intersection: `A`
   - Enter Destination Intersection: `C`
   - Output: Suggested Route: `A → B → C`

6. **Manage Vehicles at Intersection (Stack)**  
   Simulates vehicles entering and leaving an intersection using a stack.  
   **Example:**  
   - Input: `6`
   - Add Vehicle: `Car1`
   - Remove Vehicle: Last added vehicle (LIFO)

7. **Manage Traffic Queue (Queue)**  
   Simulates vehicles waiting at an intersection using a queue.  
   **Example:**  
   - Input: `7`
   - Add Vehicle: `Car2`
   - Allow Vehicle to Pass: First added vehicle (FIFO)

8. **Sort Traffic Data**  
   Sorts data like vehicle speeds or waiting times.  
   **Example:**  
   - Input: `8`
   - Select Sorting Algorithm: `Merge Sort`
   - Output: Sorted Data

9. **Search Traffic Data**  
   Searches for specific traffic-related information.  
   **Example:**  
   - Input: `9`
   - Enter Search Key: `Car3`
   - Output: Data found at position 4

10. **Exit**  
    Saves and exits the program.

## **Testing Features**
- **Display the Traffic Network:**  
  Run the program and select Option 1. Verify that the network graph matches the input data.

- **Add Intersections and Roads:**  
  Test Options 2 and 3 by adding intersections and roads. Confirm that the new nodes and edges appear in the graph.

- **Detect Bottlenecks:**  
  Create a cycle in the network and use Option 4 to confirm its detection.

- **Suggest Routes:**  
  Use Option 5 to find routes between intersections. Manually validate the results.

- **Vehicle Management:**  
  Test Options 6 and 7 by adding and removing vehicles. Ensure stacks and queues behave as expected.

- **Sort and Search Data:**  
  Use Options 8 and 9 to sort and search traffic data. Verify the results with test datasets.
