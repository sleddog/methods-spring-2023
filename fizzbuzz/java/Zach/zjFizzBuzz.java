public class zjFizzBuzz {
    public static void main(String[] args) {
        
        int n = Integer.parseInt(args[0]); 
	    int m;
	
	    if(args.length == 1){
		    m = 1;
	    }else{
		    m = Integer.parseInt(args[1]);
	    }
        for(int i = m; i <= n; i++) {
            
            if(i % 3 == 0) {
                System.out.print("Fizz");
            }
            if (i % 5 == 0) {
                System.out.print("Buzz");
            }
            if(i % 7 == 0){
                System.out.print("Ping");
            }
            if(i % 11 == 0){
                System.out.print("Pong");
            }
            if ((i % 3 != 0) && (i % 5 != 0) && (i % 7 != 0) && (i % 11 != 0)) {
                System.out.print(i);
            }
            System.out.println();
        }
    }
};
