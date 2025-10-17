#include <iostream>
#include <string>
#include <filesystem>
#include <fstream>

namespace fs = std::filesystem;
using std::cout, std::cin, std::endl, std::string, std::getline, std::stoi, std::ofstream;

int main() {
  string basePath;
  string ticketNumber;
  string claimDetailKey;
  string table;
  string column;
  string value;

  cout << "Enter file path (where folder should be created): ";
  getline(cin, basePath);

  cout << "Enter Ticket Number: ";
  getline(cin, ticketNumber);

  cout << "Enter Claim Detail Key: ";
  getline(cin, claimDetailKey);

  cout << "Enter Table Name: ";
  getline(cin, table);

  cout << "Enter Column Name: ";
  getline(cin, column);

  cout << "Enter Value: ";
  getline(cin, value);

  fs::path folderPath = fs::path(basePath) / ticketNumber;

  try {
    fs::create_directories(folderPath);
    fs::path sqlFilePath = folderPath / (ticketNumber + "_Rollout.sql");
    ofstream outFile(sqlFilePath);
    if (!outFile) {
      cout << "Error: Unable to create SQL file." << endl;
      return 1;
    }

    outFile << "SET DEFINE OFF;" << endl;
    outFile << endl;
    outFile << "UPDATE crs." << table << endl;
    outFile << "SET " << column << " = '" << value << "'" << endl;
    outFile << "WHERE CLAIM_DETAIL_KEY IN (" << claimDetailKey << ");" << endl;
    outFile << endl;
    outFile << "COMMIT;" << endl;

    outFile.close();
    cout << "Complete" << endl;
  } catch (const std::filesystem::filesystem_error& e) {
    cout << "Filesystem error: " << e.what() << endl;
    return 1;
  }

  return 0;
}
