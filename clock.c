// Digital Clock
// Pull current time from OS
// Output the time to terminal
// Hr:Min:Sec
// 24 hr based system

#include <stdio.h>
#include <windows.h> // For POSIX systems like Mac and Linux use <unistd.h>
#include <time.h>
#include <stdbool.h>

int main()
{
    time_t timeNow = time(NULL);

    struct tm localTime, *utcTime;
    localtime_s(&localTime, &timeNow);
    utcTime = gmtime(&timeNow);

    int hourDiff = (localTime.tm_hour) - (utcTime->tm_hour);
    int minDiff = (localTime.tm_min) - (utcTime->tm_min);

    char timezoneStr[10];
    snprintf(timezoneStr, sizeof(timezoneStr), "GMT%+03d:%02d", hourDiff, minDiff);

    int count = 0;

    while (count < 60)
    {
        system("cls");
        printf("Your current time (%s): \n", timezoneStr);
        printf("%02d:%02d:%02d\n", localTime.tm_hour, localTime.tm_min, localTime.tm_sec);
        Sleep(1000);
        time_t timeNow = time(NULL);
        localtime_s(&localTime, &timeNow);
        count++;
    };

    return 0;
}