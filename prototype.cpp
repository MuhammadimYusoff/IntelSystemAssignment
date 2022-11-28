// This is the testing code for system logic made by Fadwa and translated to Python by Lazeena
#include <iostream>
using namespace std;

int main() 
{
    char name[5] = {'A', 'L', 'A', 'D', 'L'};
    char user[5];
    // char name[5] = {'A', 'L', 'A', 'D', 'L'}; // goalState
    // char user[5] = {'A','L','A','D','L'}; // currentState (then compare currentState with goalState)
    int gn = 0; // no of tries
    int hn = 0; // wrong letters
    int fn = 0; // f(n) = g(n) + h(n)

    int points = 0;

    do
    {
        hn = 0;
        gn++;
        cout << "enter the name that have the meaning(The Utterly Just)\n";

        for (int i = 0; i < 5; i++)
        {
            cin >> user[i];
        }

        for (int i = 0; i < 5; i++)
        {
            if (user[i] != name[i])
                hn++;
        }

        for (int i = 0; i < 5; i++)
        {
            cout << user[i];
        }

        cout << "\nwrong letters " << hn << "\n";
        cout << "\ntries: " << gn << "\n";
        fn = gn + hn;
        cout << "\nf(n) " << fn << "\n";

        if (hn > 0)
            cout << "Try Again\n";
        else
        {
            cout << "RIGHT, you got it!\n";
            points++;
            cout << "Your score: " << points;
        }

    } while (hn != 0);
    return 0;
}
