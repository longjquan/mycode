下面注悉内容为简单的go执行系统命令
package main

import (
        "fmt"
//        "os/exec"
//	"strings"
//        "io/ioutil"
	"regexp"
	"os"
	"io"
	"bufio"
	"strconv"
)
func main(){
//	cmdd :="/bin/bash -c ps -h"
//	res :=execCmd(cmdd)
//	fmt.Println(string(res))
	path :="/access.log"
	analyLog(path)
	//phones :=analyLog(path)
	//fmt.Println(string(phones))
	}
/*
func execCmd(cmdd string) ([]byte ) { 
	args := strings.Split(cmdd, " ") 
	cmd := exec.Command(args[0], args[1:]...)
	stdout,err :=cmd.StdoutPipe() 
		if err!=nil{
		fmt.Println("错误1",err)
		}
	cmd.Start()
	bytess,err :=ioutil.ReadAll(stdout)
		if err !=nil{
		fmt.Print("错误2",err)
		return nil
		}
	return  bytess
	}
*/
func analyLog(path string) {    //([]byte){
	f,err :=os.Open(path)
	if err !=nil{
		fmt.Println("打开文件错误",err)
		return
		}
	defer f.Close()
	reader :=bufio.NewReader(f)
	filee,err :=os.Create("/phones.txt")
	fff :=bufio.NewWriter(filee)
        defer filee.Close()
	reg,_ :=regexp.Compile("1[0-9]{10}")
	phone_maps := make(map[string]string)
	for {
		line,_,err :=reader.ReadLine()
		if err ==io.EOF{
			break	
			}
		phone := reg.FindString("`"+string(line)+"`")
                if len(phone) !=0 {
      //      	fff.Write([]byte(phone +"\n"))
		phone_maps[phone] = phone  
              }
	}
	for k,_ :=range phone_maps {
		fff.Write([]byte(k+"\n"))	
	}
	fff.Flush()
	fmt.Println("不重复号码数量："+strconv.Itoa(len(phone_maps)))
	return
}

