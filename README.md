# MPU6050
Raspberry Pi Pico(Arduino開発環境)でMPU6050から読み取った角速度・加速度から角度を推定しPC上でキューブを回転させる

## ■Raspberry Pi Pico側
MPU6050/MPU6050.ino

Raspberry Pi Pico側はArduino開発環境を使用します。
Arduino開発環境にはearlephilhower版を使用しました。

以下のライブラリを使用しています。
〇角速度・加速度から角度を推定 -> MadgwickAHRSフィルタ
https://github.com/arduino-libraries/MadgwickAHRS

〇タイマー割込み
https://github.com/khoih-prog/RPI_PICO_TimerInterrupt


## ■PC側
MPU6050.py

Pythonで作成しています。

PCとPicoのシリアル通信のためにpyserialを使用しています。
以下のコマンドでインストールしてください。

pip install pyserial

3D表示のためにPanda3Dを使用しています。
以下のコマンドでインストールしてください。

pip install Panda3D

COM_PORT変数は適切なポートに書き換えてください。

