package com.tictactoe;

class Result {
    private boolean finished;
    private String result;

    public Result(boolean finished, String result){
        this.finished = finished;
        this.result = result;
    }

    public boolean getFinished(){
        return this.finished;
    }

    public String getResult(){
        return this.result;
    }
}

public class Table {

    private char[][] state;

    private int size;
    private char c;

    public Table(){
        this.size = 3;
        this.c = '-';
        this.resetState();
    }

    private void resetState(){
        this.state = new char[size][size];
        for(int i=0 ; i<size ; i++){
            for(int j=0 ; j<size ; j++){
                this.state[i][j] = this.c; // TODO: Change to numbers
            }
        }
    }

    public void printState(){
        for(int i=0 ; i<size ; i++){
            for(int j=0 ; j<size ; j++){
                System.out.print(state[i][j] + " ");
            }
            System.out.println();
        }
    }

    private int[] idxToCoord(int idx){
        int[] res = new int[2];

        res[0] = (idx-1) / 3;
        res[1] = (idx-1) % 3;

        return res;
    }

    // Put piece
    public void putPiece(int input, char c){ // TODO: handle invalid positions

        int[] res = this.idxToCoord(input);

        this.state[res[0]][res[1]] = c;
    }

    // TODO: check if works
    public boolean checkInputInRange(int input){
        if(input < 1 || input > Math.pow(size, 2)){
            return false;
        }
        return true;
    }

    // TODO
    public boolean checkInputFree(int input){
        int[] r = this.idxToCoord(input);

        if(this.state[r[0]][r[1]] == this.c){
            return true;
        }

        return false;
    }

    // TODO: check end -> Win/Draw/Loss (bool + Enum?)
    public Result checkEnd(){

        for (int i = 0; i < 3; i++) {
            if (this.state[i][0] != this.c && this.state[i][0] == this.state[i][1] && this.state[i][1] == this.state[i][2]) {
                return new Result(true, String.valueOf(this.state[i][0]));
            }
            if (this.state[0][i] != this.c && this.state[0][i] == this.state[1][i] && this.state[1][i] == this.state[2][i]) {
                return new Result(true, String.valueOf(this.state[0][i]));
            }
        }

        // Comprobar diagonales
        if (this.state[0][0] != this.c && this.state[0][0] == this.state[1][1] && this.state[1][1] == this.state[2][2]) {
            return new Result(true, String.valueOf(this.state[0][0]));
        }
        if (this.state[0][2] != this.c && this.state[0][2] == this.state[1][1] && this.state[1][1] == this.state[2][0]) {
            return new Result(true, String.valueOf(this.state[0][2]));
        }

        // Comprobar si hay espacios vacíos
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (this.state[i][j] == this.c) {
                    return new Result(false, "Ongoing");
                }
            }
        }

        // Si no hay ganador ni espacios vacíos, es empate
        return  new Result(true, "Draw");
    }
}


    // Show Swing JavaFX