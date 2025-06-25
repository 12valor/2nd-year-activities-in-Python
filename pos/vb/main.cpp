#include <iostream>

using namespace std;

int main() {
    //Declare variables
    int decimal = 0;   //input
    int bit_0 = 0;     // LSB
    int bit_1 = 0;
    int bit_2 = 0;
    int bit_3 = 0;     // MSB

    //Prompt the user to enter a decimal number (0-15)
    cout << "Enter Decimal (0-15): ";
    cin >> decimal;

    int originalDecimal = decimal;
    bit_0=decimal % 2;
    decimal=decimal / 2;
    bit_1=decimal % 2;
    decimal=decimal / 2;
    bit_2=decimal % 2;
    decimal=decimal / 2;
    bit_3=decimal % 2;
    decimal=decimal / 2;

    //Display
    cout << "The binary equivalent of " << originalDecimal << " is: ";
    cout << bit_3 << bit_2 << bit_1 << bit_0 << endl;  //print ang bit sa chakto nga order

    return 0;
}
