// Run in browser console

var input = `3   4
4   3
2   5
1   3
3   9
3   3`

var processedInput = input.split('\n').map(x => x.split('  '))

var counter = {}

for(var n2 of processedInput.map(x => parseInt(x[1]))) {
    counter[n2] = (counter[n2] || 0) + 1
}

var similarityScore = processedInput.map(x => parseInt(x[0])).map(x => x * (counter[x] || 0)).reduce((x,y) => x + y, 0)

console.log(similarityScore)
