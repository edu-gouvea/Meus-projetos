import java.util.Scanner;

public class Atividade {
    
    public static void PrintaMatriz(int matriz[][], int n){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                System.out.print(String.format("%2d", matriz[i][j]) + " ");
            }
            System.out.println();
        }
        return;
    }
    public static int[][] MatrizTransposta(int matriz[][], int n){
        int[][] transposta = new int[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                transposta[i][j] = matriz[j][i];
            }
        }
        return transposta;
    }
    public static int ProdutoDiagonalP(int matriz[][], int n){
        int produto = 1;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (i == j){
                    produto *= matriz[i][j];
                }
            }
        }
        return produto;
    }
    public static int ProdutoDiagonalS(int matriz[][], int n){
        int produto = 1;
        for (int i = 0, j = n - 1; i < n; i++, j--){
            produto *= matriz[i][j];
        }
        return produto;
    }
    public static int determinante2x2(int matriz[][]){
        return matriz[0][0] * matriz [1][1] - matriz [0][1] * matriz[1][0];
    }
    public static int determinante3x3(int matriz[][]){
        int principal1 = matriz[0][0] * matriz[1][1] * matriz[2][2]; 
        int principal2 = matriz[0][1] * matriz[1][2] * matriz[2][0]; 
        int principal3 = matriz[0][2] * matriz[1][0] * matriz[2][1]; 

        int secundaria1 = matriz[0][2] * matriz[1][1] * matriz[2][0];
        int secundaria2 = matriz[0][0] * matriz[1][2] * matriz[2][1]; 
        int secundaria3 = matriz[0][1] * matriz[1][0] * matriz[2][2]; 

        return (principal1 + principal2 + principal3) - (secundaria1 + secundaria2 + secundaria3); 
    }
    public static int determinante4x4(int matriz[][]){
        int determinante = 0;
        int aux[][] = new int[3][3];
        for (int k = 0; k < 4; k++){
            int a = 0, b = 0;
            for (int i = 1; i < 4; i++){
                b = 0;
                for (int j = 0; j < 4; j++){
                    if (j != k){
                        aux[a][b] = matriz[i][j]; 
                        b++;
                    }
                }
                a++;
            }
            int sinal = (k % 2 == 0) ? 1 : -1;
            determinante += sinal * matriz[0][k] * determinante3x3(aux); 
        }
        return determinante;
    }
    public static int determinante5x5(int matriz[][]){
        int determinante = 0;
        int aux[][] = new int[4][4];
        for (int k = 0; k < 5; k++){
            int a = 0, b = 0;
            for (int i = 1; i < 5; i++){
                b = 0;
                for (int j = 0; j < 5; j++){
                    if (j != k){
                        aux[a][b] = matriz[i][j]; 
                        b++;
                    }
                }
                a++;
            }
            int sinal = (k % 2 == 0) ? 1 : -1;
            determinante += sinal * matriz[0][k] * determinante4x4(aux); 
        }
        return determinante;
    }
    public static int[] SomaAcimaAbaixo(int matriz[][], int n){
        int somaabaixo = 0, somaacima = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (j > i){
                    somaacima += matriz[i][j];
                }
                if (i > j){
                    somaabaixo += matriz[i][j];
                }
            }
        }
        int somas[] = {somaacima, somaabaixo};
        return somas;
    }
    public static int AcimaMaior(int somas[]){
        if (somas[0] > somas[1]){
            return 2;
        }else if (somas[0] < somas[1]){
            return 1;
        }else{
            return 0;
        }
    }
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);

        int n;
        while (true){
            System.out.print("Digite o valor do índice: ");
            n = teclado.nextInt();
            if (n >= 2 && n <= 5){
                break;
            }else{
                System.out.println("valor fora do intervalo, digite outro");
            }
        }

        int matriz[][] = new int[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                matriz[i][j] = (int)(Math.random() * 19 -9);
            }
        }
        
        System.out.println("\nMatriz:");
        PrintaMatriz(matriz, n);

        System.out.println("\nMatriz transposta:");
        int transposta[][] = MatrizTransposta(matriz, n);
        PrintaMatriz(transposta, n);
        
        System.out.println("\nProduto da diagonal principal: " + ProdutoDiagonalP(matriz, n));
        
        System.out.println("\nProduto da diagonal secundária: " + ProdutoDiagonalS(matriz, n));

        if (n == 2){
            System.out.println("\nDeterminante 2x2: " + determinante2x2(matriz));
        }else if (n == 3){
            System.out.println("\nDeterminante 3x3: " + determinante3x3(matriz));
        }else if (n == 4){
            System.out.println("\nDeterminante 4x4: " + determinante4x4(matriz));
        }else if (n == 5){
            System.out.println("\nDeterminante 5x5: " + determinante5x5(matriz));
        }

        int somas[] = SomaAcimaAbaixo(matriz, n);
        int maior = AcimaMaior(somas);
        System.out.println("\nSoma dos elementos acima da diagonal principal: " + somas[0]);
        System.out.println("Soma dos elementos abaixo da diagonal principal: " + somas[1]);
        if (maior == 2){
            System.out.println("Soma acima da diagonal é maior: " + somas[0] + " > " + somas[1]);
        }else if(maior == 1){
            System.out.println("Soma abaixo da diagonal é maior: " + somas[1] + " > " + somas[0]);
        }else{
            System.out.println("São iguais: " + somas[1] + " = " + somas[0]);
        }
        teclado.close();
    }
}
