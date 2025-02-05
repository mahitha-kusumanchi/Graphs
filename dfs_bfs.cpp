/*dfsRecursive*/
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

/*dfsIterative*/

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

void dfsIterative(int start, vector<vector<int>>& adj, vector<bool>& visited) {
    stack<int> s;
    s.push(start);

    while (!s.empty()) {
        int node = s.top();
        s.pop();

        if (!visited[node]) {
            visited[node] = true;
            cout << node << " ";

            // Push neighbors in reverse order for correct traversal
            for (auto it = adj[node].rbegin(); it != adj[node].rend(); ++it) {
                if (!visited[*it]) {
                    s.push(*it);
                }
            }
        }
    }
}

int main() {
    int V = 5;
    vector<vector<int>> adj(V);
    
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 4};
    adj[3] = {1};
    adj[4] = {1, 2};

    vector<bool> visited(V, false);
    cout << "DFS (Iterative): ";
    dfsIterative(0, adj, visited);

    return 0;
}

/* bfsIterative*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfsIterative(int start, vector<vector<int>>& adj, vector<bool>& visited) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main() {
    int V = 5;
    vector<vector<int>> adj(V);
    
    adj[0] = {1, 2};
    adj[1] = {0, 3, 4};
    adj[2] = {0, 4};
    adj[3] = {1};
    adj[4] = {1, 2};

    vector<bool> visited(V, false);
    cout << "BFS (Iterative): ";
    bfsIterative(0, adj, visited);

    return 0;
}

