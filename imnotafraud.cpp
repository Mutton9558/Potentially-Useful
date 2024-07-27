// This was my answer for the FizzBuzz test. I can code.

#include <iostream>
#include <cmath>

int main() {

    for(int i = 1; i < 101; i++){
        if (i % 15 == 0){
            std::cout << "FizzBuzz";
        }
        else if (i % 3 == 0){
            std::cout << "Fizz";
        }
        else if (i % 5 == 0){
            std::cout << "Buzz";
        }
        else{
            std::cout << i;
        }
        
        if (i < 100){
            std::cout << ", ";
        }
    }

    return 0;
}
