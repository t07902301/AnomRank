
#include <iostream>
#include <fstream>
using namespace std;

int main () {
    // ofstream myfile;
    // myfile.open ("pred.txt");
    // int attack[2]={true,false};
	// for (int i = 0; i < 2; i++){
    //     myfile<<attack[i];
    // }
    // myfile.close();
    // sprintf(command, "python %s %s %s", "auc.py", 'pred.txt', 'gt.txt');
    sprintf(command, "python %s %s %s", "auc.py", "pred.txt", "gt.txt");

    return 0;
}