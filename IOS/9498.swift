//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

import Foundation

let line = readLine() ?? ""
let score = Int(line) ?? 0

switch score{
  case 90...100: //90 ~ 100 = A
    print("A")
  case 80..<90: // 80 ~ 90 = B
    print("B")
  case 70..<80: // 70 ~ 80 = C
    print("C")
  case 60..<70: // 60 ~ 70 = D
    print("D")
default: // 나머지는 F
  print("F")
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// swift 개발자 다른 사람의 코드 형식
//1번 
let line = readLine()
if let temp = line{
    if let value = Int(temp){
    if value >= 90{
        print("A")
    }
    else if value >= 80{
        print("B")
    }
    else if value >= 70{
        print("C")
    }
    else if value >= 60{
        print("D")
    }
    else{
        print("F")
    }
    }
}
///////////////////////////////////////////////////

import Foundation

var testScore = readLine()

if let testScore = testScore {
    let myScore = Int(testScore)!
    
    
    if (myScore >= 0 && myScore <= 100)
{
    switch myScore 
    {
        case 90...100:
            print("A")
        case 80...89:
            print("B")
        case 70...79:
            print("C")
        case 60...69:
            print("D")
        default:
            print("F")
    }
}
}