package org.example;

public class Person {
    String name;
    int age;

    // Constructor

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void greet() {
        System.out.println("Hello my name is "+name+", I am "+age+" years old");
    }
}
