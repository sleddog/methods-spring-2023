if ! command -v node &> /dev/null
then
    echo "The command 'node' was not found. Please install nodejs."
    exit
fi

if ! command -v npm &> /dev/null
then
    echo "The command 'npm' was not found. Please install npm."
    exit
fi

if ! command -v tsc &> /dev/null
then
    echo "The command 'tsc' was not found. Please install typescript."
    exit
fi

npm i --silent

echo "Compiling main.ts..."

tsc main.ts

echo "Compiled main.ts to main.js"
echo "Please run fizzbuzz.sh with an argument to run the program."
echo "Example: ./fizzbuzz.sh 10"
