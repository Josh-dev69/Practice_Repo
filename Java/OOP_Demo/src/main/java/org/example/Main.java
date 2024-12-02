package org.example;

public class Main {
    public static void main(String[] args) {

        Car car = new Car("Mercedez", "Benz", 2022);
        Person person1 = new Person("Ebube Titus", 20);

        car.printDetails();
        person1.greet();

        System.out.println();

        Circle circle1 = new Circle();
        circle1.printDetail();
    }
}