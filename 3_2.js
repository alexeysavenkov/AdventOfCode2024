// Run in browser console

var input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

var regex = /mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))/gm

var allMatches = input.matchAll(regex)

var result = 0

var isDo = true

for(var match of allMatches) {
    console.log(match)
  if(match[3]) {
    isDo = true
  } else if(match[4]) {
    isDo = false
  } else if(isDo) {
      result += match[1] * match[2]
  }
}
