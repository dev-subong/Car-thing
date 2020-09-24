def main(datainput, time, line, file):
    file = open("data.txt","w+")
    file.write("input line %d\r\n" %(line) +"data inputted: " %(datainput) +" time since start : " %(time))
