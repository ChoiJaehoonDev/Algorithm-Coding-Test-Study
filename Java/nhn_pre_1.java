package Java;

import java.util.Scanner;

public class nhn_pre_1{

    public boolean dfs(int y, int x){
        return false;

    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int i = 0;
        int j = 0;
        int n = scanner.nextInt();
        int [][]board = new int[10][10];

        
        for(i=0; i<n; i++){
            for (j=0; j< n; j++){
                board[i][j] = scanner.nextInt();
            }
        }
    }

}