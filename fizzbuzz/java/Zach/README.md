# FizzBuzz Java Write-up #
Zach Jewett March 21, 2023

## Runing the Program ##
To Compile to .class binary:
    javac zjFizzBuzz.java

To run code from Java file:
    navigate to respective directory and run:
    
        cd .\fizzbuzz\java\Zach\
        java zjFizzBuzz.java [int]

    run from home directory:

        java .\fizzbuzz\java\Zach\zjFizzBuzz.java [int]


To run code from bash shell:

    navigate to respective directory and run:
        cd .\fizzbuzz\java\Zach
        ./FizzBuzzShell.sh [int]

where [int] is an integer of your choosing that is passed to serve
as the FizzBuzz iteration closing condition


post-note: "java1" was required as the directory name to prevent an
"unauthorized package name" exception.

## Unit Tests ##

To do unit test you can follow the same steps above but with run_tests.sh.


To run code from bash shell:

    navigate to respective directory and run:
        cd .\fizzbuzz\java\Zach
        ./run_tests.sh


## Java Code ##

```java
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
```

