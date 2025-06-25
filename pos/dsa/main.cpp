#include <iostream>
#include <vector>
#include <string>

using namespace std;

void countingSortWeights(vector<pair<string, int>>& arr, int maxWeight) {
    vector<vector<pair<string, int>>> count(maxWeight + 1);

    for (const auto& person : arr) {
        count[person.second].push_back(person);
    }

    int index = 0;
    for (int i = 0; i <= maxWeight; i++) {
        for (const auto& person : count[i]) {
            arr[index++] = person;
        }
    }
}

int main() {
    vector<pair<string, int>> arr = {
        {"AG", 73}, {"Bob", 65}, {"Charlie", 85},
        {"David", 70}, {"Eve", 60}, {"Frank", 78}
    };
    int maxWeight = 100;

    countingSortWeights(arr, maxWeight);

    for (const auto& person : arr) {
        cout << person.first << " " << person.second << "kg" << endl;
    }

    return 0;
}
