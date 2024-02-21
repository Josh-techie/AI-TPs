#include <stdio.h>

void print_stars(int amount_stars) {
    for (int i = 0; i < amount_stars; i++) {
        printf("*");
    }
}

void print_spaces(int amount_spaces) {
    for (int i = 0; i < amount_spaces; i++) {
        printf(" ");
    }
}

void display(int tree_length) {
    int amount_stars = 1;

    for (int i = 0; i < tree_length; i++) {
        print_spaces(tree_length - i - 1);
        print_stars(amount_stars);
        printf("\n");
        amount_stars += 2;
    }
}

int main() {
    int tree_length;
    printf("Give me the tree length you want to display: ");
    scanf("%d", &tree_length);
    display(tree_length);
    return 0;
}