#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <set>

using namespace std;

typedef pair<int,int> jugs;

void printState(jugs node){
    cout<<"{"<<node.first<<","<<node.second<<"}"<<endl;
}

bool checkSol(jugs node, int n){
    // cout<<"NODE:";
    // printState(node);
    if(node.first == n || node.second == n)
        return true;
    return false;
}



jugs emptyX(jugs node){
    node.first = 0;
    return node;
}

jugs emptyY(jugs node){
    node.second = 0;
    return node;
}

jugs fillX(jugs node, int cap_x){
    node.first = cap_x;
    return node;
}

jugs fillY(jugs node, int cap_y){
    node.second = cap_y;
    return node;
}

jugs x_to_y(jugs node, int cap_y){
    int pour = min(node.first, (cap_y - node.second));
    node.first = node.first - pour;
    node.second = node.second + pour;
    return node;
}

jugs y_to_x(jugs node, int cap_x){
    int pour = min(node.second, (cap_x - node.first));
    node.first = node.first + pour;
    node.second = node.second - pour;
    return node;
}

vector<jugs> genChildren(jugs node, int cap_x, int cap_y){
    vector<jugs> children;
    if(node.first != 0)
        children.push_back(emptyX(node));
    if(node.second != 0)
        children.push_back(emptyY(node));
    if(node.first != cap_x)
        children.push_back(fillX(node, cap_x));
    if(node.second != cap_y)
        children.push_back(fillY(node, cap_y));
    if(node.first != cap_x || node.second != cap_y){
        if(node.first != 0)
            children.push_back(x_to_y(node,cap_y));
        if(node.second != 0)
            children.push_back(y_to_x(node, cap_x));
    }

    return children;

}

    

void BFS(jugs node, int cap_x, int cap_y, int sol){
    queue<jugs> nodeList;
    nodeList.push(node);
    
    set<jugs> visited;

    jugs liveNode;
    vector<jugs> children;

    while(!nodeList.empty()){
        liveNode = nodeList.front();
        if(checkSol(liveNode, sol)){
            cout<<"Solution Found"<<endl;
            return;
        }
        visited.insert(liveNode);
        nodeList.pop();
        children = genChildren(liveNode, cap_x, cap_y);
        for(auto i : children){
            // cout<<"Child";
            // printState(i);
            if(!visited.count(i))
                nodeList.push(i);
        }
    }

    cout<<"No possible outcome"<<endl;
}


int main(){
    jugs state = {0,4};
    int capacity_x = 3;
    int capacity_y = 4;
    
    BFS(state, capacity_x,capacity_y, 2);
}