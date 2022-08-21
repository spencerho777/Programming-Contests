/*
ID: spencewert
LANG: C++
PROG: convention
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

std::ifstream fin("convention.in");
ofstream fout("convention.out");

int n, m, c;

bool validate(int interval, vector<int> cows, int n, int m , int c) {
    int buses = 1;
    int first = cows.front();
    int occ = 1;
    int x = 1;
    while( (buses <= m) && (x < n)) {
        if( (occ < c) && (cows[x] - first <= interval)) {
            occ++;
        }
        else {
            buses++;
            first = cows[x];
            occ = 1;
        }
        x++;
    }
    if( (x < n) || (buses > m)) return false;
    return true;
}

int main() {
    fin >> n >> m >> c;

    vector<int> cows;
    int input;
    for(int a=0; a<n; a++) {
        fin >> input;
        cows.push_back(input);
    }
    sort(cows.begin(), cows.end());

    int lo = 1;
    int hi = pow(10, 9);

    while(lo < hi - 1) {
        int mid = (lo+hi) / 2;
        if (validate(mid, cows, n, m, c)) hi = mid;
        else lo = mid;
    }
    //cout << hi << endl;
    fout << hi;
}