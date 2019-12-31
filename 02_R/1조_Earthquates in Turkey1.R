setwd("C:/Users/202-017/Documents/data")
library(dplyr)
library(readxl)
library(ggplot2)
install.packages('corrplot')
library(corrplot)
library(stringr)

eq <- read.csv('earthquake.csv')

head(eq2)
str(eq2)
summary(eq2)

head(eq)



eq <- eq[,-c(1,3,6,7,8,9,10,15)]
#eq$date <- str_replace_all('.','-',eq$date)
#eq$date <- as.Date(eq$date)


eqcorr2 <- cor(eq[,-1])
eqcorr2
corrplot(eqcorr2, method='shade',tl.col='black', tl.srt=45)


ggplot(eq,aes(x=xm,y=ms))+geom_col(aes(fill=ms))
# 다양한 방법으로 지진정도를 측정했을 때의 최대값은 ms의 경우 5가 제일 많다.
ggplot(eq,aes(x=xm,y=mb))+geom_col(aes(fill=mb))

ggplot(eq,aes(x=xm,y=depth))+geom_col(aes(fill=xm))
ggplot(eq,aes(x=xm,y=richter))+geom_point()

a <- tapply(eq2$richter,eq2$country,sum)
a <- sort(a)
a

b <- tapply(eq2$richter,eq2$city,sum)
b <- sort(b)
b

ggplot(eq, aes(depth, long, color = as.factor(richter>6)))+
  geom_line()

ggplot(eq, aes(lat, long, color = as.factor(richter)))+
  geom_line()


ggplot(eq2, aes(country, xm, color = as.factor(richter)))+
  geom_col()
