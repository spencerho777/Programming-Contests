
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

std::ifstream fin("a2real.txt");
ofstream fout("a2out.txt");

int t;

// bool validate(int interval, vector<int> cows, int n, int m , int c) {
//     if( (x < n) || (buses > m)) return false;
//     return true;
// }

bool isStartX(vector<char> w) {
    auto firstX = find(w.begin(), w.end(), 'X');
    auto firstO = find(w.begin(), w.end(), 'O');
    bool onX;
    if (firstO == w.end() || (firstX - w.begin() < firstO - w.begin() && firstX != w.end())) {
        onX = true;
    }
    else {
        onX = false;
    }
    return onX;
}

long long solve(int n, vector<char> w) {
    bool onX = isStartX(w);
    bool prevStartX = onX;

    long long cnt = 0;
    long long total = 0;

    vector<char> xo;
    vector<int> xoind;

    for (int ind = 0; ind < w.size(); ++ind) {

        if (w[ind] == 'X'|| w[ind] == 'O') {
            xo.push_back(w[ind]);
            xoind.push_back(ind);
        }

        if (onX && w[ind] == 'O') {
            cnt++;
            onX = false;
        }
        else if (!onX && w[ind] == 'X') {
            cnt++;
            onX = true;
        }
        total += cnt;
        //cout << cnt << "\n";
    }

    if (xo.size() == 0) {
        return 0;
    }
    //cout << "First total: " << total << "\n";

    //cout << prevStartX << " " << (xo.front() == 'X') << "\n";
    bool currStartX;
    long long result = 0;
    for (int i = 0; i < n-1; i++) {
        currStartX = (xo.front() == 'X');
        if (currStartX != prevStartX) {
            prevStartX = currStartX;
            total -= n - xoind.front();
        }
        if (total <= 0) {
            break;
        }
        //cout << total << " ";
        result += total;
        
        if (w.front() == xo.front()) {
            xo.erase(xo.begin());
            xoind.erase(xoind.begin());
        }
        w.erase(w.begin());
    }
    //cout << "\n";
    return result % 1000000007;
}

int main() {
    fin >> t;

    for (int a=0; a<t; a++) {
        int n;
        vector<char> w;
        fin >> n;
        char c;
        for (int b=0; b<n; b++){
            fin >> c;
            w.push_back(c);
        }
        long long solution = solve(n, w);

        fout << "Case #" << a+1 << ": " << solution << "\n";
        //cout << solve(n, w) << " <-- result" << "\n";
        //cout << "Case #" << a+1 << ": " << solution << "\n";
    }
    
}