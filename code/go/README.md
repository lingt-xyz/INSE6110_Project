# Methods for the Cryptanalysis of Substitution Ciphers

A Fast Method for the Cryptanalysis of Substitution Ciphers by Thomas Jakobsen

## Compile

- GNU/Linux: `go build`
- Windows: `env GOOS=windows GOARCH=amd64 go build`

## How to run it

You can find binaries in [Release](https://github.com/lingt-xyz/INSE6110_Project/releases).

### Parameters

- `-c`: cipher opetion; should be `encipher`, `decipher` or `demo`. Required.
- `-i`: input file. Required.
- `-k`: key used to enciper. Optional. If not provided, a random key would be given.
- `-v`: verbose output. Optional.

### Examples

> Use `substitutionDeciphers.exe` if you are on a Windows system.

- Encipher

```shell script
./substitutionDeciphers -c=encipher -i=p1 -v=true
./substitutionDeciphers -c=encipher -i=p2 -k=TPULEMYNOKXDCAHFJSIRGBVQWZ -v=true
./substitutionDeciphers -c=encipher -i=p3
```

- Decipher

```shell script
./substitutionDeciphers -c=decipher -i=c1
./substitutionDeciphers -c=decipher -i=c2
./substitutionDeciphers -c=decipher -i=c3 -v=true
```

- Encipher and Decipher
```shell script
./substitutionDeciphers -c=demo -i=d1
./substitutionDeciphers -c=demo -i=d2
./substitutionDeciphers -c=demo -i=d3 -v=true
```
