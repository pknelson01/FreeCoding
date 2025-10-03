#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream> 

/* To handle spaces and punctuation:
   if (c = cipher.end()) {
      result << in[i];
   }

   Unrelated: 
      Endless input loop:
         while (input("Word: ", word)) {
            blah blah blah
         }

      -- Make sure you #include "input.h"
*/

using std::cout, std::endl, std::cin, std::string, std::map, std::ifstream, std::istringstream, std::ofstream;

int main() {
   map<char, char> aToS;
   map<char, char> sToA;
   string alphabet = "abcdefghijklmnopqrstuvwxyz";
   string scramble = "qwzeryhtapjglndkvxoubicfms";
   string line;

   for (size_t i = 0; i < alphabet.length(); i++) {
      aToS[alphabet[i]] = scramble[i];
      aToS[alphabet[i] - 'a' + 'A'] = scramble[i] - 'a' + 'A';
   }

   for (size_t i = 0; i < alphabet.length(); i++) {
      sToA[scramble[i]] = alphabet[i];
      sToA[scramble[i] - 'a' + 'A'] = alphabet[i] - 'a' + 'A';
   }

   // for (auto &entry : aToS) {
   //    cout << entry.first << " - " << entry.second << endl;
   // }

   // for (auto &entry : sToA) {
   //    cout << entry.first << " - " << entry.second << endl;
   // }

   ifstream inFile("scrambled_nemiksManifesto.txt");
   if (!inFile) return 1;

   ofstream outFile("nemiksManifesto.txt");
   if (!outFile) return 1;

   while (getline(inFile, line))  {
      for (char &c : line) {
         auto key = sToA.find(c);
         if (key != sToA.end()) {
            cout << "Before reassignment: " << c;
            c = key->second;
            // cout << " - After reassignment: " << c << endl;
         }
      }
      outFile << line << endl;
   }
   cout << "Decoding complete. Output written to nemiksManifesto.txt" << endl;
}