let Input=[10, 5, 20, 8]
// Output: 20


function largestNum(input){
    console.log(Math.max(...input))
}
largestNum(Input)


function larNum(input){
    let largest=input[0]
    for(let i=1;i<input.length;i++){
        if(input[i]>largest){
            largest=input[i]
        }
    }
    return largest
}

console.log(larNum(Input))