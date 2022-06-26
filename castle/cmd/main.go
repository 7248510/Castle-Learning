package main
//go mod init github.com/7248510/castle
import (
	"cmd/networking"
	"log"
	"fmt"
)

func main() {
	//I have to read the documentation but without capitalizing the function names in http.go the functions were not found
	srv2 := networking.TestMe(456)
	fmt.Println("Duplicate value: " ,srv2)
	networking.Test()
	srv := networking.NewHTTPServer(":8080")
	log.Fatal(srv.ListenAndServe())
	//Fix #1 see logicError.png (Great example of one)
	/* 
	Pretty cool, but this API only accepts base64 as the post request. Decoding the values with cyberchef revealed:
	Let's Go #1
	Let's Go #2
	Let's Go #3
	The Windows curl commands are do not work out of the box. An alternative is WSL, VM/Container or Git bash:

	curl -X POST IP:8080 -d '{"record": {"value": "SGVsbG8gd29ybGQ="}}' = Accepted
	curl -X GET IP:8080 -d '{"offset": 0}'
	*/
}
