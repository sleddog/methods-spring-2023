
# FizzBuzz in Typescript

Fizzbuzz is a simple programming problem where you print out every number up to n, with the caveat that if a number is divisible by 3 you print the word Fizz, by 5 you print Buzz, and by both you print FizzBuzz. My solution to this problem was written in Typescript.


## Documentation

```typescript
function main(): void {
  let arg: number = parseInt(process.argv[2], 10);
  if (isNaN(arg)) {
    console.error("Please specify a number");
    process.exit(1);
  }
  for (let i = 1; i <= arg; i++) {
    console.log(fizzbuzz(i));
  }
}

function fizzbuzz(n: number): string {
  if (n % 15 === 0) return "FizzBuzz";
  if (n % 3 === 0) return "Fizz";
  if (n % 5 === 0) return "Buzz";
  return n.toString();
}

main();
```
The above code is my solution to this problem. The main function simply checks to make sure the input is a number, then loops from 1 to that number. Inside this loop, the fizzbuzz function is called for each number in the loop.

The fizzbuzz function is where the actual calculations come in. The most important part of this function is the use of the modulo or % operator. This operator essentially outputs the remainder if you were to divide the two numbers. If the output is a 0, that means the first number is divisible by the second number. I used this with if statements to check if the number is divisible by 3, 5, or 15 since 15 is divisible by both 3 and 5. I could've probably made this faster by only having if statements for 3 and 5 then concatenating the strings together if fizz was already part of the output string. The reason I didn't do this was because I felt this was more readable and easier to understand. The fizzbuzz function then returns a string to the main function to be printed.

## Instructions

In the root of the git repository run:

```bash
  cd fizzbuzz/typescript/Skeegan123
```

Compile the TS file with the compile script (Note this requires Node, npm, and Typescript to be installed on your system):

```bash
  ./compileFizzbuzz.sh
```

Run the program with a number passed in:

```bash
  ./fizzbuzz.sh 10
```

And you are done!

**Note:** This requires both Typescript and Node to be installed. The compileFizzbuzz.sh script checks for these dependancies and will exit if one is not detected with an error message telling you to install whichever dependancy is needed.

**Another Note:** The compileFizzbuzz.sh script first checks for dependancies with the "command" command. It then runs:

```bash
  npm i --silent
  tsc main.ts
```

**Final Note:** The fizzbuzz.sh script first checks if node is installed. Then, it checks that main.ts was compiled by looking for the existance of main.js. It then checks if a number was supplied as an argument, if not, it defaults to 25. Finally, the script then runs the command:

```bash
  node main.js $num
```