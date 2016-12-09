package main

import(
	"fmt"
)

func sqrt(x float64) float64{
	var z float64 = float64(x)
	for i :=0;i<10;i++{
		z = z- (z*z -x)/(2*z)
	}
	return z
}

func main(){
	fmt.Println(sqrt(2))
}
