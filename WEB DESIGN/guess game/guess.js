
const randomNumber =Math.floor(math.random()*100)
console.log(randomNumber)
let attempt = 0;

function checkGuess(){
    const guess =parseInt(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess)|| guess< 1 || guess >100){
        setmessage("please enter a number between 1 and 100")
        return;
    }
    if(guess === randomNumber){
        setMessage("congratulations!!you have guessed correctly")
        document.getElementById("guessfield").disabled= true;
    }
     else if (guess<randomNumber){
        setMessage("too low.Try again")
    }
    else 
        setMessage("very high.Try again")

    }
        
     function setMessage(message){
        document.getElementById("message").textContent = message
    }
        
    
