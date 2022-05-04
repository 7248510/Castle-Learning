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

## Capitalization Explained:
`
You may have noticed that all of the declarations in the greet.go file you called were capitalized. Go does not have the concept of public, private, or protected modifiers like other languages do. External visibility is controlled by capitalization. Types, variables, functions, and so on, that start with a capital letter are available, publicly, outside the current package. A symbol that is visible outside its package is considered to be exported.
`
* [How To Write Packages in Go](https://www.digitalocean.com/community/tutorials/how-to-write-packages-in-go)

## Credit
* [How to Use Go Modules](https://www.digitalocean.com/community/tutorials/how-to-use-go-modules)
* Distributed Services with Go by Travis Jeffery
