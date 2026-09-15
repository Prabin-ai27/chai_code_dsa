let Input=[10, 5, 20, 8]
// Output: 5

function smailNumMin(input){
    console.log(Math.min(...input))
}

smailNumMin(Input)


function smallnumberFoorLoop(input){
    let smallerNum=input[0]
    for(let i=1;i<input.length;i++){
        if(smallerNum>input[i]){
            smallerNum=input[i]
        }
    }
    return smallerNum
}
console.log(`Smaller number use for loop :- ${smallnumberFoorLoop(Input)}`)



function smallNumRue(input){
    return input.reduce((small,current)=>{
        return small<current?small:current
    })
}
console.log(`Smaller number use reduce :-${smallNumRue(Input)}`)