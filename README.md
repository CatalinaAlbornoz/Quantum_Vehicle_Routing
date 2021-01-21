# Quantum_Vehicle_Routing
Applying quantum computing to tackle Vehicle Routing Problems

The objective of this project is to apply the quantum vehicle routing solution to real problems such as vaccine distribution.

To learn more about the Vehicle Routing Problem (VRP) please check out the notebook in the VRP folder.

I first looked for possible encodings of the problem and found that some encodings were very efficient in terms of the number of Qubits but not in terms of Quantum Volume. Considering that we are in the NISQ era and that Quantum Volume is a very limiting factor if you want high accuracy, I decided to go for the encoding that was most efficient in terms of Quantum Volume. This meant using the QUBO (Quantum Unconstrained Binary Optimization) encoding.

By trying to solve the problem I soon realized that current QVRP solutions were highly unaccurate, even for a small number of nodes. For 5 nodes (4 clients and one depot) and 2 vehicles I needed 24 qubits. Even though I used a 32 qubit simulator the results were rather poor. Hence I decided to change strategy.

One solution that is not optimal but which can get us close to the result we need is approximating the problem to a collection of Traveling Salesman Problems (TSP). The solution consists the  on clustering the clients and then addressing each client as a single TSP. This largely simplifies the problem. This solution was applied to a collection of public data on the location of vaccination posts at one department in Colombia. Note that these are not necessarily COVID vaccination locations and the dataset may be outdated, but it gives us a sense of how well this solution works. The dataset can be downloaded here: https://www.datos.gov.co/Salud-y-Protecci-n-Social/Puestos-de-vacunaci-n-de-Risaralda-Puntos-de-vacun/8cw5-iyp3

