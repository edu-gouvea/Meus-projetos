import java.util.Scanner;
public class mergesort {
    
    public static void mergeSort(int ar[]){
        int quant = ar.length;
        
        if (quant < 2){
            return;
        }

        int mid = quant / 2;
        int esq[] = new int[mid];
        int dir[] = new int[quant - mid];

        for (int i = 0; i < mid; i++){
            esq[i] = ar[i];
        }
        for (int i = mid; i < quant; i++){
            dir[i - mid] = ar[i];
        }

        mergeSort(esq);
        mergeSort(dir);

        merge(ar, esq, dir);

    }

    public static void merge(int ar[], int esq[], int dir[]){
        int quantesq = esq.length;
        int quantdir = dir.length;

        int i = 0, j = 0, k = 0;

        while (i < quantesq && j < quantdir){
            if (esq[i] <= dir[j]){
                ar[k] = esq[i];
                i++;
            }else{
                ar[k] = dir[j];
                j++; 
            }
            k++;
        }

        while (i < quantesq){
            ar[k++] = esq[i++];
        }
        while (j < quantdir){
            ar[k++] = dir[j++];
        }
    }
    public static void printaVetor(int ar[]){
        for (int i: ar){
            System.out.print(i + " ");
        }
    }
    
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite o tamanho do vetor: ");
        int n = teclado.nextInt();
        
        int ar[] = new int[n];
        
        System.out.print("Digite o valor mínimo que pode ser assumido dentro do vetor: ");
        int min = teclado.nextInt();
        System.out.print("Digite o valor máximo que pode ser assumido dentro do vetor: ");
        int max = teclado.nextInt();


        for (int i = 0; i < n; i++){
            ar[i] = (int)(Math.random() * (max - min + 1) + min);
        }
        
        printaVetor(ar);
        System.out.println();
        
        mergeSort(ar);

        printaVetor(ar);
        System.out.println();

        teclado.close();
    }
}
