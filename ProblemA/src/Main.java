import java.util.*;

public class Main {
    public static void main(String[] args) {

    }

    public static void ABC278() {
        Scanner sc = new Scanner(System.in);
        String[] nk = sc.nextLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);
        Queue<String> aList = new ArrayDeque<>(List.of(sc.nextLine().split(" ")));
        for (int i = 0; i < k; i++) {
            aList.remove();
            aList.add("0");
        }
        for (int i = 0; i < n; i++) {
            System.out.print(aList.remove() + " ");
        }
        System.out.println();
    }

    public static void ABC279() {
        Scanner sc = new Scanner(System.in);
        String[] line = sc.nextLine().split("");
        int tipCount = 0;
        for (String valuable : line) {
            if (valuable.equals("v")) {
                tipCount+=1;
            } else {
                tipCount+=2;
            }
        }
        System.out.println(tipCount);
    }
    public static void ABC280() {
        Scanner sc = new Scanner(System.in);
        String[] hw = sc.nextLine().split(" ");
        int h = Integer.parseInt(hw[0]);
        int result = 0;
        for (int i = 0; i < h; i++) {
            List<String> lineList = new ArrayList<>(List.of(sc.nextLine().split("")));
            int countPawn = (int) lineList.stream().filter( l -> l.equals("#")).count();
            result += countPawn;
        }
        System.out.println(result);
    }
    public static void ABC281() {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        for (int i = 0; i <= n; i++) {
            System.out.println(n-i);
        }
    }
    public static void ABC282() {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        for (int i = 0; i < n; i++) {
            System.out.print((char)(65 + i)); //小文字の場合は97
        }
        System.out.println();
    }
    public static void ABC283() {
        Scanner sc = new Scanner(System.in);
        String[] sArray = sc.nextLine().split(" ");
        int a = Integer.parseInt(sArray[0]);
        int b = Integer.parseInt(sArray[1]);
        System.out.println((int) Math.pow(a,b));
    }
    public static void ABC284() {
        Stack<String> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        for(int i = 0; i < n ; i++ ) {
            String line = sc.next();
            stack.push(line);
        }
        for(int i = 0; i < n ; i++ ) {
            System.out.println(stack.pop());
        }
    }

    public static void ABC285() {
        Scanner sc = new Scanner(System.in);
        String[] sArray = sc.nextLine().split(" ");
        int a = Integer.parseInt(sArray[0]);
        int b = Integer.parseInt(sArray[1]);
        String result = "No";
        if (a*2 == b || a*2+1 == b) {
            result = "Yes";
        }
        System.out.println(result);
    }
}

