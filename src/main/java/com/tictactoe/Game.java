package com.tictactoe;

import java.util.Scanner;


enum Turn {
    X(true), 
    O(false);

    boolean turn;

    Turn(boolean turn){
        this.turn = turn;
    }

    public boolean getTurn(){
        return this.turn;
    }

    public char getXO(){
        if(this.turn){
            return 'X';
        }
        return 'O';
    }

    public void change(){
        this.turn = !this.turn;
    }
}

public class Game {

    private Table table;
    private Turn turn;

    private Scanner sc = new Scanner(System.in);

    public Game(){
        this.table = new Table();
        this.turn = Turn.X;
    }

    public void start(){
        int input = 0; // TODO: struct for the input + valid??
        boolean valid = false;

        Result r;

        this.table.printState(); // Empty table

        do{
            System.out.println("Player " + this.turn.getXO() + " (1 to 9): "); // TODO: depend on the range

            while (!valid || input == 0) {
                try {
                    input = Integer.parseInt(this.sc.nextLine());
                    valid = true; // La conversión fue exitosa

                    // TODO: Check range and free position
                    if (!this.table.checkInputInRange(input)) {
                        System.out.println("El número está fuera de rango.");
                        input = 0;
                    }else if(!this.table.checkInputFree(input)){
                        System.out.println("La posición está ocupada.");
                        input = 0;
                    }
                } catch (NumberFormatException e) {
                    System.out.println("Entrada inválida. Por favor, introduce un número entero.");
                }
            }
            
            // Write input
            this.table.putPiece(input, this.turn.getXO());

            // Change turn
            this.turn.change();

            // Reset input
            input = 0;
            valid = false;

            // Show
            this.table.printState();

            r = this.table.checkEnd();
        }
        while(!r.getFinished());

        // Announce result
        System.out.println("\n" + r.getResult());
    }
}

