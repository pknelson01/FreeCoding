#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream> 

using std::cout, std::cin, std::endl, std::ifstream, std::string, std::map, std::istringstream;

int main() {
   ifstream inFile("sampleText.txt");
   if (!inFile) {
      return 1;
   }

   map <int, string> nemiksManifesto;
   string line;
   string word;
   int index = 0;
   int wordCounter = 0;
   while (getline(inFile, line)) {
      istringstream words(line);
      while (words >> word) {
         nemiksManifesto[index] = word;
         index++;
         wordCounter++;
      }
   }
   inFile.close();
   
   for (auto &entry : nemiksManifesto) {
      cout << "{key: " << entry.first << " - value: '" << entry.second << "'}" << endl;
   }

   cout << "Total words in this text: " << wordCounter << endl;
   
   return 0; 
}