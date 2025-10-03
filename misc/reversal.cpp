#include <iostream>
#include <string>
#include <stack>
#include <cctype>

using std::cout, std::endl, std::cin, std::stack, std::string, std::tolower;

int main() {
    stack<char> reversal;
    string response;
    cout << "Enter a word: ";
    cin >> response;
    
    for (auto l : response) {
        reversal.push(tolower(l));
    }

    while (!reversal.empty()) {
        cout << reversal.top();
        reversal.pop();
    }
    cout << endl;
}