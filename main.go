package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
)

func main() {
    // 获取环境变量中的端口，如果没有则默认使用 8080
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    // 定义处理函数
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "Hello, World!")
    })

    // 在所有网络接口上监听
    address := "0.0.0.0:" + port
    fmt.Printf("Server running on %s...\n", address)
    if err := http.ListenAndServe(address, nil); err != nil {
        log.Fatal(err)
    }
} 