import Foundation


let value = readLine()! // 이것을 옵셔널을 받게 된다. 


// spring 값이기 때문에 일반적으로 
let array = value.components(separatedBy: " ")


print("\(Int(array[0])! + Int(array[1])!)")

// swift는 MVC 패턴이 있다.
// MVC 패턴으로 IOS 기반 코딩을 한다.

// View
func inputView() -> String {
  return 
}