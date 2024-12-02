package org.example;

public class Car {
    String  brand;
    String model;
    int year;

    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void printDetails() {
        System.out.println("Your Car brand is "+ brand);
        System.out.println("The model is "+ model);
        System.out.println("It was designed in year " + year);
    }
}
