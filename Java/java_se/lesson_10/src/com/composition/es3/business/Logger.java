package com.composition.es3.business;

public class Logger {
    private Output output;

    public Logger(Output output) {
        // A runtime, sarà ConsoleOutput o FileOutput
        this.output = output;
    }

    public Output getOutput() {
        return output;
    }
}
