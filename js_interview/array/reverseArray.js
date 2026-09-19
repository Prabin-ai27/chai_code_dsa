let Input=[1, 2, 3, 4, 5]
//  Output: [5, 4, 3, 2, 1]

let output=[]

for(let i=Input.length-1;i>=0;i--){
    output.push(Input[i])
}

console.log(output)