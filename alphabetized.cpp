#include <iostream>
#include <functional>
#include <string>
#include <cctype>
#include <queue>
#include <vector>

using std::cout, std::cin, std::endl, std::string, std::greater, std::getline, std::tolower, std::toupper, std::priority_queue, std::vector;

int main() {
  string response;
  priority_queue<string, vector<string>, greater<string>> alpha;

  while (true) {

    cout << "Enter a word: ";
    getline(cin, response);

    if (response.empty()) {
      break;
    }

    for (int i = 0; i < response.size(); i++) {
      response[i] = tolower(response[i]);
    }

    alpha.push(response);
  }

  while (!alpha.empty()) {
    cout << alpha.top() << endl;
    alpha.pop();
  }
}