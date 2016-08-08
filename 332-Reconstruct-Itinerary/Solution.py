public class Solution {
    public List<String> findItinerary(String[][] tickets) {
        HashMap<String, multiset
    }
}
class Solution {
private:
    void traverse(string from, vector<string>& route, unordered_map<string, multiset<string>>& port_map)
    {
        while(port_map[from].size())
        {
            auto next = port_map[from].begin();
            port_map[from].erase(next);
            traverse(*next, route, port_map);
        }
        route.push_back(from);
    }
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) 
    {
        unordered_map<string, multiset<string>> port_map;
        for(auto& pair: tickets) port_map[pair.first].insert(pair.second);
        vector<string> route;
        traverse("JFK", route, port_map);
        return vector<string>(route.rbegin(), route.rend());
    }
};