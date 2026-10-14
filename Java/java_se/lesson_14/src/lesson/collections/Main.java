package lesson.collections;

interface Methods {
    void method1();

    // Solo metodi static e default DEVONO avere un corpo
    default void method2() {
            method3();
    };
    static void method3() {
        System.out.println("method3 implementato");
    };
}

abstract class AbstractClass implements Methods {
    abstract void method4();
    @Override
    public void method1() {
        System.out.println("method1 override");
    }
    // È possibile overridare anche il default
    @Override
    public void method2() {
        System.out.println("method2 override");
    }

    // Non è possibile invece overridare i metodi static in quanto implicitamente final
//    @Override
//    public void method3() {
//        System.out.println("method3 override");
//    }
}

public class Main extends AbstractClass {
    static void main(String[] args) {
        AbstractClass ac = new Main();
        ac.method1();
        ac.method2();
        Methods.method3();
        ac.method4();
    }

    // È necessario overridare TUTTI i metodi senza corpo, sia interfacce che classi astratte

    @Override
    public void method1() {
        System.out.println("method1");
    }

    @Override
    public void method2() {
        System.out.println("method2");
    }

    @Override
    void method4() {
        System.out.println("method4");
    }
}