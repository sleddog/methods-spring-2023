import java.io.*;
import java.util.*;
import java.util.Scanner;

class fizbuz{
	public static void main(String[] args){
		
		//Original fizbuz
		// int n = Integer.parseInt(args[0]);	

		// for(int i = 1; i<=n; i++){

		// 	if(i % 5 == 0 && i % 3 == 0){
		// 		System.out.println("Fizzbuzz ");
		// 	}else if (i % 5 == 0){
		// 		System.out.println("Buzz");
		// 	}else if (i % 3 == 0){
		// 		System.out.println("Fizz");
		// 	}else	{
		// 		System.out.println(i);
		// 	}
		// }


        /*
         * Unnecessarily convoluted FizzBuzz++ program that accepts any number of command line integers, where
         * the last integer, is used as the iteration termination condition. Any preceding integers are assigned to a 
         * LinkedHashMap, where their values are used as keys for hardcoded FizzBuzz words. If the number of arguments exceed
         * the number of keywords, the keywords are reset, and used with an asterick added. Conversely, if there are fewer 
		 * arguments not all keywords are used. The map is iterated over for each whole number in range 1 to n. If the 
         * remainder of the key divided by the iteration number is zero, the respective value is concatenated to a string. 
         * The string is printed to the console. If the string is empty it retuns the iteration number.
         */
        
		 int n = Integer.parseInt(args[args.length-1]);	//Last cl argument passed in is used as iterator condition
		 String fizzBuzzVocabArr[] = {"Fizz", "Buzz", "Ping", "Pong"};   //keywords for FizzBuzz
		 LinkedHashMap<Integer, String> fizzBuzzMap = new LinkedHashMap<>(); //LinkedList maintains insertion order
 
 
		 for(int i = 0; i < args.length - 1; i++) {  //builds key value pairs
			 int key = Integer.parseInt(args[i]);
			 String value = null;
			 try{
				 value = fizzBuzzVocabArr[i];
			 }
			 catch(Exception e) {    //catches out of bounds exceptions, resets iterator, adds annotation
				 System.out.println("Arguments exceed key words, annotating keywords.");
				 value = fizzBuzzVocabArr[i % 4] + "*";
			 }
			 finally {   
				 fizzBuzzMap.put(key, value);
			 }
		 }
 
		 
		 for(int j = 1; j <= n; j++) {   //i
			 String str = "";				
			 for(int keyVal : fizzBuzzMap.keySet() ) {	//iterate over list of keys used
				 if(j % keyVal == 0) {
					 String word = fizzBuzzMap.get(keyVal);
					 str = str + word;
				 }
			 }
			 if(str.equals("")) {
				 System.out.println(j);
			 }
			 else{
				 System.out.println(str);
			 }
		 }
		 
	 }//end main
 }//end class


