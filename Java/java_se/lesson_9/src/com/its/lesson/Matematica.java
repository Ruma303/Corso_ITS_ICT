package com.its.lesson;
/*
* Creare una classe Matematica che contiene 4 metodi utilizzando le regole di overloading
* possibilmente con promozione del tipo
* */

public class Matematica {
    public static int somma(int a, int b){
        return a+b;
    }

    public static double somma(double a, double b) {
        return a+b;
    }

    public static int somma(int a, long b) { // Casting esplicito
        return a + (int)b;
    }

    public static double somma(int a, double b) {
        return a+b; // int è promosso automaticamente a double
    }
}
