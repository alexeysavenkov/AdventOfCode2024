// Run in browser console

var input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

var regex = /mul\((\d+),(\d+)\)/gm

var allMatches = input.matchAll(regex)

var result = 0

for(var match of allMatches) {
  result += match[1] * match[2]
}
