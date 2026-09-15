Input=[10, 5, 20, 8, 20]
// Output: 10

function secLargestNumberFor(input){
    let maxNum=input[0]
    let secNum=input[0]
    for(let i=1;i<input.length;i++){
        if(input[i]<maxNum){
            secNum=maxNum
            maxNum=input[i]
        }
        else if(input[i]<secNum && input !== maxNum){
            secNum=input[i]
        }
    }
    return secNum
}
console.log(`Second largest Number ${secLargestNumberFor(Input)}`)