library(dplyr)
library(ggplot2)

eq <- read.csv('D:\\RData\\earthquake.csv')
str(eq)
head(eq$time)

dim(eq)

colSums(is.na(eq))
eq <- eq[,-c(1,3,7,8,9,10,15)]

names(eq)


qplot(eq$ms, eq$mb)

qplot(eq$country)
qplot(eq$long)
qplot(eq$lat)
qplot(eq$depth)
qplot(eq$xm)
qplot(eq$md)
qplot(eq$richter)
qplot(eq$ms)

dat <- eq %>% group_by(country) %>% summarise(mean_xm=mean(xm), mean_md=mean(md), mean_ms=mean(ms), mean_r = mean(richter), n=n())

dat <- as.data.frame(dat)
dat_or <- dat[order(-dat$mean_r),]
dat_or


ggplot(data=dat_or, aes(x=reorder(dat_or$country,-dat_or$mean_r), y=dat_or$mean_r)) + geom_col()

table(eq$country)

ggplot(data=eq, aes(x=eq$country, y=eq$lat)) + geom_boxplot()

class(eq$date)

eq <- eq[order(eq$date),]
head(eq)


eq$year <- substring(eq$date, 1, 4)
names(eq)
head(eq$year,20)

dat2 <- eq %>% group_by(year) %>% summarise(mean_y_ri = mean(richter), n=n())
dat2 <-data.frame(dat2)

ggplot(dat2, aes(x=year, y=mean_y_ri, group=1)) + geom_line()
ggplot(dat2, aes(x=year, y=n, group=1)) + geom_line()
