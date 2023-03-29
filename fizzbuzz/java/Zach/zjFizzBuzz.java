public class zjFizzBuzz {
    public static void main(String[] args) {
        
        int n = Integer.parseInt(args[0]);

        for(int i = 1; i <= n; i++) {
            if(i % 3 == 0 && i % 5 == 0 && i % 7 == 0 && i % 11 == 0) {
                System.out.println("FizzBuzzPingPong");
            }else if(i % 3 == 0 && i % 5 == 0 && i % 7 == 0){
                System.out.println("FizzBuzzPing");
            }else if(i % 3 == 0 && i % 5 == 0 && i % 11 == 0){
                System.out.println("FizzBuzzPong");
            }else if(i % 3 == 0 && i % 7 == 0 && i % 11 == 0){
                System.out.println("FizzPingPong");
            }else if(i % 5 == 0 && i % 7 == 0 && i % 11 == 0){
                System.out.println("BuzzPingPong");
            }else if(i % 3 == 0 && i % 5 == 0){
                System.out.println("FizzBuzz");
            }else if(i % 3 == 0 && i % 7 == 0){
                System.out.println("FizzPong");
            }else if(i % 3 == 0 && i % 11 == 0){
                System.out.println("FizzPing");
            }else if(i % 5 == 0 && i % 7 == 0){
                System.out.println("BuzzPing");
            }else if(i % 5 == 0 && i % 7 == 0){
                System.out.println("BuzzPong");
            }else if(i % 7 == 0 && i % 11 == 0){
                System.out.println("PingPong");
            }else if(i % 3 == 0) {
                System.out.println("Fizz");
            }else if (i % 5 == 0) {
                System.out.println("Buzz");
            }else if(i % 7 == 0){
                System.out.println("Ping");
            }else if(i % 11 == 0){
                System.out.println("Pong");
            }else {
                System.out.println(i);
            }
        }
    }
};
