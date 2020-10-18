.PHONY: targ clean eclean
targ:
# helloc: hello.c
	gcc -o helloc hello.c
	helloc
# hellocpp: hello.cpp
	g++ -o hellocpp hello.cpp
	hellocpp
# hellof90: hello.f90
	gfortran -o hellof90 hello.f90
	hellof90
# hellogo: hello.go
	go build -o hellogo.exe hello.go
	hellogo

clean:
	rm *.o

eclean:
	rm *.exe