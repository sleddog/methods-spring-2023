#FizzBuzz Java Write-up#
Zach Jewett March 21, 2023

##Runing the Program##
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


##Java Code##

```java
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
```
##Unit Tests##

To do unit test you can follow the same steps above but with an added value.
The added value is where you want to start from. To Find a single value just add the same number twice.

To Compile to .class binary:
    javac zjFizzBuzz.java

To run code from Java file:
    navigate to respective directory and run:
    
        cd .\fizzbuzz\java\Zach\
        java zjFizzBuzz.java [int] [int]

    run from home directory:

        java .\fizzbuzz\java\Zach\zjFizzBuzz.java [int] [int]


To run code from bash shell:

    navigate to respective directory and run:
        cd .\fizzbuzz\java\Zach
        ./FizzBuzzShell.sh [int]

where [int] is an integer of your choosing that is passed to serve
as the FizzBuzz iteration closing condition


post-note: "java1" was required as the directory name to prevent an
"unauthorized package name" exception.
