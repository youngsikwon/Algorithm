// 두 수 비교 하기

//문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

import Foundation

let line = readLine()!
let lineArr = line.split(separator: " ")
let a = Int(lineArr[0]) ?? 0
let b = Int(lineArr[1]) ?? 0

if a > b{
  print(">")
} else if a < b{
  print("<")

}else{
  print("==")
}