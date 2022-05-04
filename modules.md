# Working with modules
* mkdir scratch
* cd scratch
* mkdir cmd
* cd cmd
* go mod init cmd
* powershell new-item main.go (Edit the file with a simple hello world)
* go run main.go
* mkdir networking
* cd networking && powershell new-item modTest.go
* cd ../ (After you add some information to the new file)
* go run main.go



## Credit
* [How to Use Go Modules](https://www.digitalocean.com/community/tutorials/how-to-use-go-modules)
* Distributed Services with Go by Travis Jeffery
