package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class nhn_pre_1 {

    static int[] dy = { 0, 0, -1, 1 };
    static int[] dx = { -1, 1, 0, 0 };
    static int[][] board = new int[10][10];
    static int max = 0;
    static int[] size = new int[50];

    public static boolean dfs(int y, int x, int n) {
        int ny = 0;
        int nx = 0;

        for (int i = 0; i < 4; i++) {
            ny = y + dy[i];
            nx = x + dx[i];

            if (0 > ny || ny >= n || 0 > nx || nx >= n)
                continue;
                
            else {
                if (board[ny][nx] == 1) {
                    board[ny][nx] = -1;
                    max += 1;
                    dfs(ny, nx, n);
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int i = 0;
        int j = 0;
        int n = scanner.nextInt();
        int cnt = 0;
        ArrayList<Integer> list2 = new ArrayList<Integer>();

        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                board[i][j] = scanner.nextInt();
            }
        }
        
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (board[i][j] == 1){
                    max = 0;
                    if (dfs(i, j, n) == true) {

                        list2.add(max);
                        cnt += 1;
                    }
                }
            }
        }
        
        Collections.sort(list2);
        System.out.println(cnt);
        for(int x=0; x< cnt; x++){
            System.out.printf("%d ", list2.get(x));
        }
        
    }

}