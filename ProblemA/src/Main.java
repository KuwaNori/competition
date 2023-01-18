import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        
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

