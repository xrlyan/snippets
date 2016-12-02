package main

import "fmt"

func main(){
    var a int = 100
    var b int = 200
    var res int

    res = max(a,b)
    
    fmt.Printf("max value : %d\n", res)

}

func max (a,b int) int{
    var res int
    if(a>b){
        res = a
    }else{
        res = b
    }
    return res
}
