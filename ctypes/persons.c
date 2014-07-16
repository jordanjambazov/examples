#include <stdio.h>

typedef struct Person {
    char *name;
    int age;
} Person;


Person get_person(char *name, int age) {
    Person person = {name, age};
    return person;
}

int main() {
    Person person = get_person("Jordan", 21);
    printf(person.name);
    return 0;
}
