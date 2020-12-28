import Foundation 

func isItLeapYear() -> Int {
  var result: Int = 0 // 0으로 초기화
  var userInput = readLine()!
  var year:Int = 0

  year = Int(userInput)!



  
  if (year%4==0 && !(year%100 == 0) || year%400 == 0){
    result = 1
  }else{
    result = 0
  }

  return result
}

print("\(isItLeapYear())")


함수 안에 다 넣을건지, global  변수로 쓸 것인지 고민할 필요.