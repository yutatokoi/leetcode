import "fmt"
const WAIT_TIME = 10

type Logger struct {
    messageToPrintingTime map[string]int
}

func Constructor() Logger {
    logger := Logger{
        messageToPrintingTime: map[string]int{},
    }
    return logger
}

func (this *Logger) ShouldPrintMessage(timestamp int, message string) bool {
    if printingTime, hasMessage := this.messageToPrintingTime[message]; !hasMessage || printingTime + WAIT_TIME <= timestamp {
        this.messageToPrintingTime[message] = timestamp
        return true
    }
    return false
}

/**
 * Your Logger object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.ShouldPrintMessage(timestamp,message);
 */
