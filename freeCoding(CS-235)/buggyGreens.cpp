#include <iostream>
#include <string>
#include <cctype>
#include <vector>
#include <queue>
#include <stack>
#include <utility>


/*
    CONSIDER USING A PRIORITY QUEUE TO SUGGEST THE FURTHEST DISTANCE CLUB POSSIBLE FOR THIS SHOT
*/


using std::cout, std::endl, std::string, std::cin, std::isupper, std::islower, std::queue, std::vector, std::stack, std::getline, std::pair;

class GolfBag {
private:
    int putter;
    int lobWedge;
    int sandWedge;
    int gapWedge;
    int pitchingWedge;
    int nineIron;
    int eightIron;
    int sevenIron;
    int sixIron;
    int fiveIron;
    int fourIron;
    int fiveWood;
    int threeWood;
    int driver;

public:
    GolfBag() : putter(20), lobWedge(80), sandWedge(90), gapWedge(110), pitchingWedge(120), nineIron(130), eightIron(140), sevenIron(150), sixIron(160), fiveIron(170), fourIron(180), fiveWood(200), threeWood(215), driver(230) {}
    
    int getPutter() const { return putter;}
    int getLobWedge() const { return lobWedge;}    
    int getSandWedge() const { return sandWedge;}
    int getGapWedge() const { return gapWedge;}
    int getPitchingWedge() const { return pitchingWedge;}
    int getNineIron() const { return nineIron;}
    int getEightIron() const { return eightIron;}
    int getSevenIron() const { return sevenIron;}
    int getSixIron() const { return sixIron;}
    int getFiveIron() const { return fiveIron;}
    int getFourIron() const { return fourIron;}
    int getFiveWood() const { return fiveWood;}
    int getThreeWood() const { return threeWood;}
    int getDriver() const { return driver;}

    vector<pair<string, int>> getAllClubs() const {
        return {
            {"Putter", getPutter()},
            {"Lob Wedge", getLobWedge()},
            {"Sand Wedge", getSandWedge()},
            {"Gap Wedge", getGapWedge()},
            {"Pitching Wedge", getPitchingWedge()},
            {"9-Iron", getNineIron()},
            {"8-Iron", getEightIron()},
            {"7-Iron", getSevenIron()},
            {"6-Iron", getSixIron()},
            {"5-Iron", getFiveIron()},
            {"4-Iron", getFourIron()},
            {"5-Wood", getFiveWood()},
            {"3-Wood", getThreeWood()},
            {"Driver", getDriver()}
        };
    }
};

int main() {
    cout << "Welcome to Buggy Greens Golf Club!" << endl;
    GolfBag bag;
    for (auto [club, yardage] : bag.getAllClubs()) {
        cout << club << " -> " << yardage << " yards" << endl;
    }
}