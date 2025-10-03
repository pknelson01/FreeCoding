#include <iostream>
#include <string>
#include <stack>
#include <cctype>

using std::cout, std::endl, std::cin, std::stack, std::string, std::tolower, std::getline;

int main() {
    string response;
    
    while (true) {
        stack<char> reversal;
        string backwards;
        cout << "Enter a word: ";
        getline(cin, response);

        if (response.empty()) {
            break;
        }

        for (int i = 0; i < response.size(); i++) {
            response[i] = tolower(response[i]);
        }

        for (auto l : response) {
            reversal.push(l);
        }

        while (!reversal.empty()) {
            backwards += reversal.top();
            reversal.pop();
        }

        if (backwards == response) {
            cout << response << " is a palindrome!" << endl;
        } else {
            cout << response << " is not a palindrome. :(" << endl;
        }
    }
    cout << "Goodbye! :)" << endl;
}