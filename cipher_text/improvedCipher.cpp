#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream> 

using std::cout, std::endl, std::cin, std::string, std::map, std::ifstream, std::istringstream, std::ofstream;

/* TODO: to handle spaces and punctuation
   if (c = cipher.end()) {
      result << in[i];
   }

   Unrelated: 
      Endless input loop:
         while (input("Word: ", word)) {
            blah blah blah
         }

      -- Make sure you #include "input.h"

   -- Improve this cipher with the following features:
      - Create a console experience. 
         - "Would you like to scramble... "
            "... a text file? (1)"
            "... console input? (2)"
         - After scrambling, ask if you would like to decode.
*/

int scramble() {
   return 0;
}

int decode() {
   return 0;
}

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

   ifstream inFile("text.txt");
   if (!inFile) return 1;

   ofstream outFile("scrambled_nemiksManifesto.txt");
   if (!outFile) return 1;

   while (getline(inFile, line)) {
      for (char &c : line) {
         auto key = aToS.find(c);
         if (key != aToS.end()) {
            c = key->second;
         }
      }
      outFile << line << endl;
   } cout << "Encrypting complete. Output written to scrambled_nemiksManifesto.txt" << endl;

   for (size_t i = 0; i < alphabet.length(); i++) {
      sToA[scramble[i]] = alphabet[i];
      sToA[scramble[i] - 'a' + 'A'] = alphabet[i] - 'a' + 'A';
   }

   ifstream inputFile("scrambled_nemiksManifesto.txt");
   if (!inputFile) return 1;

   ofstream outputFile("nemiksManifesto.txt");
   if (!outputFile) return 1;

   while (getline(inputFile, line)) {
      for (char &c : line) {
         auto key = sToA.find(c);
         if (key != sToA.end()) {
            c = key->second;
         }
      }
      outputFile << line << endl;
   } cout << "Decoding complete. Output written to nemiksManifesto.txt" << endl;
}