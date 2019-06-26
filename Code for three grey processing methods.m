%%三种方法实现灰度化与调用MATLAB函数实现灰度化
close all;
clear all;

Img=imread('11.jpg');
[n m a]=size(Img);%判断图像的大小

GrayImage= rgb2gray(Img);%调用MATLAB函数实现灰度化

Img_Gray=zeros(n,m);
for x=1:n%通过双循环对图像进行灰度化处理
    for y=1:m
     %  Img_Gray(x,y)=max(Img(x,y,1),max(Img(x,y,2),Img(x,y,3)));  %第一种方法实现灰度化
     %  Img_Gray(x,y)=(Img(x,y,1)+Img(x,y,2)+Img(x,y,3))/3;%第二种方法实现灰度化
        Img_Gray(x,y)=0.3*Img(x,y,1)+0.59*Img(x,y,2)+0.11*Img(x,y,3);%第三种方法实现灰度化
    end
end
figure,imshow(Img);title('原图像')
figure,imshow(GrayImage);title('调用系统函数实现灰度化')
figure,imshow(uint8(Img_Gray));title('第三种方法')
