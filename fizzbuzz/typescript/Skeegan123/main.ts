export

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
  if (n % 1155 === 0) return "FizzBuzzPingPong";
  if (n % 77 === 0) return "PingPong";
  if (n % 15 === 0) return "FizzBuzz";
  if (n % 3 === 0) return "Fizz";
  if (n % 5 === 0) return "Buzz";
  if (n % 7 === 0) return "Ping";
  if (n % 11 === 0) return "Pong";
  return n.toString();
}

main();
