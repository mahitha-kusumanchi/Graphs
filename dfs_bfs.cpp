#include <iostream>
#include <vector>
using namespace std;

void dfsRecursive(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfsRecursive(neighbor, adj, visited);
        }
    }
}

int main() {
    int V = 5;
    vector<vector<int>> adj(V);
    
    // Example Graph (Undirected)
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 4};
    adj[3] = {1};
    adj[4] = {1, 2};

    vector<bool> visited(V, false);
    cout << "DFS (Recursive): ";
    dfsRecursive(0, adj, visited);  // Start DFS from node 0

    return 0;
}
