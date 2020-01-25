#include<iostream>
using namespace std;

int myFunc(int n) {
	int sum = 0;
	for (int i = 0; i < n;i++) {
		if (i % 3 == 0 || i % 5 == 0) { sum += i; }
	}
	return sum;
}
int main() {
	cout << myFunc(20) << endl;
	cin.get();
	return 0;
 }
