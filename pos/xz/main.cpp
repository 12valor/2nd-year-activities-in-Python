#include <iostream>
#include <string> //kulang

using namespace std;

int main() {
    // variables
    string first_name = "Ada"; //""
    string last_name = "Lovelace"; //""
    int age = 20;
    char sex = 'F'; //''
    double height = 1.7; //double
    double weight = 56.7; //double

    // display
    cout << "First Name: " << first_name << endl; //butangan endl
    cout << "Last Name: " << last_name << endl; //last_name dapat indi Last_name
    cout << "Age: " << age << endl;
    cout << "Sex: " << sex << endl;
    cout << "Height: " << height << " m" << endl; //butangan unit
    cout << "Weight: " << weight << " kg" << endl; //butangan unit

    return 0;
}
