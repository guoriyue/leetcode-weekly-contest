class UnionFind{
private:
    vector<int> parent;
    vector<int> rank;
    int rn;
public:
    UnionFind(int n){
        
        for(int i=0;i<n;i++){
            parent.push_back(i);
            rank.push_back(0); 
        }
        rn=n;
        
    }
    int find(int i){
        if(parent[i]!=i){
            parent[i]=find(parent[i]);
        }
        return parent[i];
    }
    void add(int a, int b){
        int roota=find(a);
        int rootb=find(b);
        if(roota!=rootb){
            if(rank[roota]<rank[rootb]){
                parent[roota]=rootb;
            }
            else if(rank[roota]>rank[rootb]){
                parent[rootb]=roota;
            }
            else{
                parent[roota]=rootb;
                rank[rootb]+=1;
            }
        }
    }
    
    int count(){
        int results=0;
        int criterion=find(0);
        for(int i=0;i<rn;i++){
            if(find(i)==criterion){
                results+=1;
            }
        }
        return results;
    }
};
using namespace std;
class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        UnionFind u(n);
        // cout<<"here";
        vector<int> exist(100005);
        int r=restricted.size();
        for(int i=0;i<r;i++){
            exist[restricted[i]]=1;
        }
        for(int i=0;i<n-1;i++){
            if(exist[edges[i][0]]==0&&exist[edges[i][1]]==0)
            {
                u.add(edges[i][0], edges[i][1]);
            }
        }
        return u.count();
    }
};
