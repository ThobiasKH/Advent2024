#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char rotate(char guard) {
    switch (guard) {
        case '^':
            return '>';

        case '>':
            return 'v';

        case 'v':
            return '<';

        case '<':
            return '^';
    }
}

int traverse(char** arr, char guard, int guardY, int guardX, int height, int width) {
    int yOffset;
    int xOffset;
    switch (guard) {
        case '^':
            yOffset = -1;
            xOffset =  0;
            break;

        case '>':
            yOffset =  0;
            xOffset =  1;
            break;

        case 'v':
            yOffset =  1;
            xOffset =  0;
            break;

        case '<':
            yOffset =  0;
            xOffset = -1;
            break;
    }

    int yDesired = guardY + yOffset;
    int xDesired = guardX + xOffset;


    arr[guardY][guardX] = 'X';
    if (yDesired < 0 || yDesired >= height || xDesired < 0 || xDesired >= width) {
        return 1;
    }

    char nextPos = arr[yDesired][xDesired];

    int isObstacle = nextPos == '#';
    int hasNotBeenTraversed = nextPos != 'X';

    char newGuard = isObstacle ? rotate(guard) : guard;
    if (isObstacle) {
        printf("%d | %d \n", guardY + 1, guardX + 1);
    }

    if (isObstacle) {
        return hasNotBeenTraversed + traverse(arr, newGuard, guardY, guardX, height, width);
    }

    return hasNotBeenTraversed + traverse(arr, newGuard, yDesired, xDesired, height, width);
    
    
}

int main() {
    const char *filename = "input.txt"; 
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }

    char buffer[1024];
    int line_count = 0;
    char **data = NULL; 

    while (fgets(buffer, sizeof(buffer), file)) {
        size_t length = strlen(buffer);
        if (buffer[length - 1] == '\n') {
            buffer[length - 1] = '\0'; 
            length--;
        }

        char *line = malloc(length + 1); 

        strcpy(line, buffer);

        char **temp = realloc(data, sizeof(char *) * (line_count + 1));
        data = temp;

        data[line_count] = line;
        line_count++;
    }

    fclose(file);

    int y;
    int x;
    char guard;
    int height = line_count;
    int width = strlen(data[0]); 
    
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (data[i][j] != '.' && data[i][j] != '#') {
                y = i;
                x = j;
                guard = data[i][j];
                break;
            }
        }
    }

    int result = traverse(data, guard, y, x, height, width); // wrong lol
    int count = 0;

    for (int i = 0; i < height; i++) { 
        for (int j = 0; j < width; j++) {
            if (data[i][j] == 'X') count++;
        }
        printf("%s | Line: %d \n", data[i], i);
    }

    for (int i = 0; i < line_count; i++) {
        free(data[i]);
    }
    free(data);

    printf("%d", count);

    return 0;
}



