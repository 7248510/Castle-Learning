# Working with modules(Examples folder)
* mkdir scratch (This is the external/root folder)
* cd scratch
* mkdir cmd (This is the location of main.go)
* cd cmd
* go mod init cmd (You have to have main.go and go.mod in the same folder)
* powershell new-item main.go (Edit the file with a simple hello world)
* go run main.go
* mkdir networking
* cd networking && powershell new-item modTest.go
* cd ../ (After you add some information to the new file)
* go run main.go



## Credit
* [How to Use Go Modules](https://www.digitalocean.com/community/tutorials/how-to-use-go-modules)
* Distributed Services with Go by Travis Jeffery
