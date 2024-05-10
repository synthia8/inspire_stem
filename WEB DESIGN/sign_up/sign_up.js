let input = document.getElementByid("inputbox");

let buttons = document.querySelectorAll("button");//gives us an array

let string ="";//makes whatever value in the input a string 
let arr = Array.from(buttons)
arr.forEach(button=>{
    button.addEventListener('click',(e)=>{
        if(e.target.innerHTML=="SIGN IN"){
            string=eval(string);
            input.value=string;
        }
    })
})