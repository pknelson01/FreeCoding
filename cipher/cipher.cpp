#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream> 

using std::cout, std::endl, std::cin, std::string, std::map, std::ifstream, std::istringstream;

int main() {
   map<char, char> cipher;
   string alphabet = "abcdefghijklmnopqrstuvwxyz";
   string scramble = "qwzeryhtapjglndkvxoubicfms";
   string unScrambled;

   for (size_t i = 0; i < alphabet.length(); i++) {
      cipher[alphabet[i]] = scramble[i];
      cipher[alphabet[i] - 'a' + 'A'] = scramble[i] - 'a' + 'A';
   }

   for (auto &entry : cipher) {
      cout << entry.first << " - " << entry.second << endl;
   }

   ifstream inFile("scrambled_nemiksManifesto.txt");
   if (!inFile) {
      return 1;
   }

   while (getline(inFile, unScrambled))  {
      
   }
}