#include <iostream>
using namespace std;

class Numbers
{
private:
    int number;
    string lessThan20[19] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
                             "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    string lessThan100[9] = {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
    string hundred = "hundred";
    string thousand = "thousand";

    string thousandText(int number)
    {
        int temp = number / 1000;
        if (temp > 0)
        {
            return lessThan20[temp - 1] + " " + thousand;
        }
        else
        {
            return "";
        }
    }

    string hundredText(int number)
    {
        int th = number / 1000;
        int temp = (number - th * 1000) / 100;
        if (temp > 0)
        {
            return lessThan20[temp - 1] + " " + hundred;
        }
        else
        {
            return "";
        }
    }

    string remainingText(int number)
    {
        int th = number / 1000;
        int hu = (number - th * 1000) / 100;
        int temp = (number - th * 1000 - hu * 100) / 10;
        int ones = number - th * 1000 - hu * 100 - temp * 10;
        if (number > 0)
        {
            if (temp * 10 >= 20)
            {
                if (ones > 0)
                {
                    return lessThan100[temp - 1] + " " + lessThan20[ones - 1];
                }
                else
                {
                    return lessThan100[temp - 1];
                }
            }
            else if ((temp + ones) > 0)
            {
                return lessThan20[(temp + ones) - 1];
            }
            else
            {
                return "";
            }
        }
        else
        {
            return "zero";
        }
    }

    string converterFunction(int number)
    {
        string t = thousandText(number);
        string h = hundredText(number);
        string rem = remainingText(number);

        return (t + " " + h + " " + rem);
    }

public:
    Numbers(int n)
    {
        number = n;
    }

    void printEnglishTranslation()
    {
        string text = converterFunction(number);
        std::cout << text << std::endl;
    }
};

int main()
{
    int n;
    std::cout << "Enter a number from 0 to 9999" << std::endl;
    std::cin >> n;
    Numbers num(n);
    num.printEnglishTranslation();
    return 0;
}