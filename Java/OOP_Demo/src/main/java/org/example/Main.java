package org.example;

public class Main {
    public static void main(String[] args) {

        Car car = new Car("Mercedez", "Benz", 2022);
        Person person1 = new Person("Ebube Titus", 20);
        Manager manager1 = new Manager("Ebube Joshua", 1, 40000.0);
        manager1.manageTeam();

        car.printDetails();
        person1.greet();

        System.out.println();

        Circle circle1 = new Circle();
        circle1.printDetail();
    }
}