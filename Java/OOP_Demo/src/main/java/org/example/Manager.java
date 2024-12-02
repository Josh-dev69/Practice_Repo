package org.example;

public class Manager extends Employee {

    public Manager(String name, int id, double salary) {
        super(name, id, salary);
    }

    public void manageTeam() {
        System.out.println(getName() + " manages the team");
    }
}
