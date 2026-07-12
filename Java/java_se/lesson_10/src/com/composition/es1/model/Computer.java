package com.composition.es1.model;

public class Computer {

    private CPU cpu;
    private RAM ram;
    private Storage storage;

    // Aggregazione semplice
    public Computer(CPU cpu, RAM ram, Storage storage) {
        this.cpu = cpu;
        this.ram = ram;
        this.storage = storage;
    }

    // Il costruttore non riceve gli oggetti pronti, ma i DATI per crearli
    public Computer(String marcaCpu, int ghz, int gbRam, String tipoDisco, int gbDisco) {
        // VERA COMPOSIZIONE: Il Computer crea da solo i suoi pezzi.
        // Se muore il Computer, queste istanze muoiono con lui.
        this.cpu = new CPU(marcaCpu, ghz);
        this.ram = new RAM(gbRam);
        this.storage = new Storage(tipoDisco, gbDisco);
    }

    public String descriviConfig() {
        return "CPU: " + this.cpu + ", RAM: " + this.ram + ", STORAGE: " + this.storage;
    }

    public CPU getCpu() {
        return cpu;
    }

    public RAM getRam() {
        return ram;
    }

    public Storage getStorage() {
        return storage;
    }

    public void testPerformace() {
        cpu.verificaPerformace();
        ram.verificaPerformace();
        storage.verificaPerformace();
    }
}
