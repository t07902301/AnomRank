g++ -std=c++11 -O3 main.cpp -o anomrank;
# The last parameter in the command when running anomrank execution file is the name of dataset used. This one is only for storing the groudtruth and anomScore files.
./anomrank "darpa.txt" " " 60 256 0 50 70 "darpa"