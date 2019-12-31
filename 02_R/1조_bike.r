######################################
########### ¾çÇÑ¼Ö ##################

bike <- read.csv("C:\\Program Files\\R\\R-3.6.1\\bike-sharing-demand\\train.csv")
install.packages("gridExtra")
library(gridExtra)
library(ggplot2)
library(dplyr)

bike$season <- as.character(bike$season)
bike$holiday <- as.character(bike$holiday)
bike$workingday <- as.character(bike$workingday)
bike$weather <- as.character(bike$weather)

b1 <- qplot(bike$season)
b2 <- qplot(bike$holiday)
b3 <- qplot(bike$workingday)
b4 <- qplot(bike$weather)
grid.arrange(b1,b2, b3,b4, ncol=4, nrow=1)

str(bike)
head(bike)
summary(bike)

a1 <- qplot(bike$temp)
a2 <- qplot(bike$atemp)
a3 <- qplot(bike$windspeed)
a4 <- qplot(bike$humidity)
grid.arrange(a1,a2, a3,a4, ncol=4, nrow=1)


qplot(bike$casual)
qplot(bike$registered)
qplot(bike$count)


ggplot(data = bike, aes(x=temp, y=atemp)) + geom_point()
ggplot(data = bike, aes(x=temp, y=atemp, col=season)) + geom_point()


c1 <- ggplot(data = bike, aes(x=season, y=temp)) + geom_boxplot()
c2 <- ggplot(data = bike, aes(x=season, y=windspeed)) + geom_boxplot()
c3 <- ggplot(data = bike, aes(x=season, y=humidity)) + geom_boxplot()
grid.arrange(c1,c2, c3, ncol=3, nrow=1)



d1 <- ggplot(data = bike, aes(x=weather, y=temp)) + geom_boxplot()
d2 <- ggplot(data = bike, aes(x=weather, y=windspeed)) + geom_boxplot()
d3 <- ggplot(data = bike, aes(x=weather, y=humidity)) + geom_boxplot()
grid.arrange(d1,d2, d3, ncol=3, nrow=1)


qplot(bike$weather)
ggplot(data = bike, aes(x=weather, y=count)) + geom_boxplot()

qplot(bike$season)
ggplot(data = bike, aes(x=season, y=count)) + geom_col()
ggplot(data = bike, aes(x=season, y=count)) + geom_boxplot()

qplot(bike$holiday)
ggplot(data = bike, aes(x=holiday, y=count)) + geom_boxplot()

qplot(bike$workingday)
ggplot(data = bike, aes(x=workingday, y=count)) + geom_boxplot()


hour <- substr(bike$datetime,12,13 )
year <- substr(bike$datetime,1,4)
month <- substr(bike$datetime,6,7)
day <- substr(bike$datetime,9,10)

head(year)
head(hour)
head(month)
head(day)

bike$year <- year
bike$hour <- hour
bike$month <- month
bike$day <- day

names(bike)


q1 <- ggplot(data = bike, aes(x=year, y=count)) + geom_col()  
q2 <- ggplot(data = bike, aes(x=year, y=casual)) + geom_col()
q3 <- ggplot(data = bike, aes(x=year, y=registered)) + geom_col()
grid.arrange(q1,q2, q3, ncol=3, nrow=1)


ggplot(data = bike, aes(x=hour, y=count, fill=workingday)) + geom_col()
work_1 <- bike %>% filter(workingday == 1)
work_0 <- bike %>% filter(workingday == 0)
w2 <- qplot(hour,count,data = work_1, geom = "boxplot")
w3 <- qplot(hour,count,data = work_0, geom = "boxplot")
grid.arrange(w2, w3, ncol=2, nrow=1)


ggplot(data = bike, aes(x=month, y=count, fill=season)) + geom_col()  
qplot(bike$count)







#######################################
##############·ù°æ¾Æ##################

getwd()
library(dplyr)
library(ggplot2)
library(readxl)
library(stringr)
library(gridExtra)

bike <- read_excel('train_bike.xlsx')
head(bike,7)

summary(bike)
str(bike)
tail(bike)

# ?Šµ?„ humidity

ggplot(bike,aes(x=season,y=temp,color=season))+geom_col()

a = ggplot(bike,aes(x=season,y=count))+geom_col()
b = ggplot(bike,aes(x=temp,y=count))+geom_col()
c = ggplot(bike,aes(x=humidity,y=count,color=humidity))+geom_col()
d = ggplot(bike,aes(x=weather,y=count))+geom_col()
grid.arrange(a,b,c,d,nrow=2,ncol=2)

ggplot(bike,aes(x=temp,y=count))+geom_col()
ggplot(bike,aes(x=windspeed,y=..density..))+geom_histogram()+geom_line(stat="density")

ggplot(bike,aes(x=season,y=..density..))+geom_line(stat='density',aes(x=temp),color='red')+
  geom_line(stat='density',aes(x=atemp),color='blue')

ggplot(bike, aes(x=season,y=temp))+geom_col()
ggplot(bike, aes(x=workingday,y=count))+geom_col()
ggplot(bike, aes(x=holiday,y=count))+geom_col()

table(bike$workingday)
table(bike$holiday)


bike$year <- as.integer(substr(bike$datetime,1,4))
bike$month <- as.integer(substr(bike$datetime,6,7))
bike$hour <- as.integer(substr(bike$datetime,12,13))

ggplot(bike, aes(x=as.factor(month),y=count))+
  geom_boxplot()
ggplot(bike, aes(x=as.factor(hour),y=count))+
  geom_boxplot()+ggtitle("24?‹œê°? ??€?—¬?Ÿ‰ë¶„í¬") #ì¶œê·¼?‹œê°„ì— ì¦ê?€?–ˆ?‹¤ê°€ ?‡´ê·¼ì‹œê°„ì— ?˜?‹¤?‹œ ì¦ê?€


p1 = ggplot(bike, aes(x=as.factor(month),y=casual))+
  geom_boxplot()+xlab("month")
p2 = ggplot(bike, aes(x=as.factor(month),y=registered))+
  geom_boxplot()+xlab("month")
grid.arrange(p1,p2,nrow=2)


p3 = ggplot(bike, aes(x=as.factor(hour),y=casual))+
  geom_boxplot()+xlab("hour")
p4 = ggplot(bike, aes(x=as.factor(hour),y=registered))+
  geom_boxplot()+xlab("hour")
grid.arrange(p3,p4,nrow=2)

