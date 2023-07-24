**项目名称**：数云控 - 一种用于数控设备的泛用性云监控IOT平台

**核心技术栈**：Vue3、Flask、PyQT5、MySQL、Redis、Axios、Vuex、Element-Plus、less、WebSocket、JWT、Flask-restful、Nginx等

**项目描述**：该项目为一种泛用性数控设备云监控平台，集泛用、监管、控制三位一体至云端。用户可以通过平台实时上传G代码工程文件至云端并推送至工控客户端来实现实时控制硬件，并在平台上实时开启远程视频流监控录像。同时平台还提供了全平台统一账户注册、工具下载、设备调参、进程监管、远程监控等多种功能。

**项目亮点**：
- 后端 采用 JWT 授权进行通信，登录状态设定生命周期验证
- 利用 WebSocket 协议基于设备码和 FormData 实现工程文件三端传输并在工控端解析载入硬件系统控制。
- 利用 WebSocket 协议基于 Base64 + OpenCV 实现工控软件到后端在到游览器的视频帧通信
- 使用 PyQT5 + Pymysql 实现工控设备客户端的开发; 并使用 Serial通信 + Threading多线程控制 来实现多命令的并发硬件监控

**上线地址**：http://cnc-iot-system.panzer-jack.cn/

**视频演示**：https://www.bilibili.com/video/BV17X4y1n7GF/


