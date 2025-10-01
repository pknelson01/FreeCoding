#include <iostream>
#include <string>
#include <queue>
#include <cctype>

using std::cout, std::endl, std::string, std::getline, std::cin, std::queue, std::tolower;

int main() {
    string response;
    queue<string> line;
    int counter = 0;
    queue<string> q;

    while (true) {
        cout << "OPEN! Come on in and submit your name: ";
        getline(cin, response);
        
        if (response.empty()) {
            break;
        }

        line.push(response);
    }

    while (!line.empty()) {
        counter ++;
        q.push(line.front());
        line.pop();
    }

    cout << "Number of people in queue: " << counter << endl;
    string response_1;
    cout << "Would you like to see the full list? (Y/N) ";
    getline(cin, response_1);


    if (!response_1.empty() && std::toupper(response_1[0]) == 'Y') {
        int x = 1;
        auto q_copy = q;
        while (!q_copy.empty()) {
            cout << x << "). " << q_copy.front() << endl;
            q_copy.pop();
            x++;
        }
    } else if (!response_1.empty() && std::toupper(response_1[0]) == 'N') {
        cout << endl;
    } else {
        cout << "INVALID INPUT: '" << response_1 << "' " << endl;
    }
    cout << "Goodbye!" << endl;
}