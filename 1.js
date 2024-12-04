// Run in browser console

var input = `3   4
4   3
2   5
1   3
3   9
3   3`

var processedInput = input.split('\n').map(x => x.split('  '))

var sortedList1 = processedInput.map(x => parseInt(x[0]))
var sortedList2 = processedInput.map(x => parseInt(x[1])).toSorted()

console.assert(sortedList1.length == sortedList2.length)

var differences = Array.from(Array( sortedList1.length ).keys()).map(i => Math.abs(sortedList1[i] - sortedList2[i]))

var differenceSum = differences.reduce((x,y) => x + y, 0)

console.log(differenceSum)

