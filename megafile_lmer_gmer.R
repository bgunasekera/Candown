library(lme4)
library(lmerTest)
library(Rcpp)
library(plyr)
library(dplyr)
library(tidyr)

rt <- read.csv("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/reaction_time.csv")
df <- read.csv("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/df.csv")

df<- df %>% mutate(ResponseButton=recode(ResponseButton, 
                         'go'="1",
                         'None'="0"))

df<- df %>% mutate(correct=recode(correct, 
                                         'True'="1",
                                         'False'="0"))

df <- transform(df, ResponseButton = as.numeric(ResponseButton))
df <- transform(df, correct = as.numeric(correct))


m <- lmer(rt_time ~ drug*Condition + (1| SubjectID/drug/Condition), data=rt)
summary(m)
anova(m)

m1 <- glmer(ResponseButton ~ drug*Condition + (1| SubjectID/drug/Condition), data=df, family="binomial")
summary(m1)

m2 <- glmer(correct ~ drug*Condition + (1| SubjectID/drug/Condition), data=df, family="binomial")
summary(m2)

