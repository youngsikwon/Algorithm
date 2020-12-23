let coordinatesX = Int(readLine()!)!
let coordinatesY = Int(readLine()!)!

if coordinatesX > 0 {
    if coordinatesY > 0 {
        print(1)
    } else {
        print(4)
    }
} else if coordinatesX < 0 {
    if coordinatesY > 0 {
        print(2)
    } else {
        print(3)
    }
}