#Notes
#Here there are two variables. 
#y variable is the change in caarms score (total/pos/neg) calculated by subtracting day 1 from day 21 for either cbd or placebo
#x variable are the contrast estimates derrived from an ROI
#The numbered are ROIs are 6 subdivisions of the insula and were obtained from here:
#  https://atlas.brainnetome.org/download.html
#This is an atlas that parcellates the brain into 246 cortical and subcortical regions
#Download file "BNA_PM_3D_246" and "BNA_subregions.xlsx"
#L_insula ROI (from line 168 on) was made myself in Pick Atlas in SPM
#From line 168 on were the codes finally agreed upon to be used in cantop analysis for symptom analysis with brain data


library(readxl)
library(ggplot2)
library(lme4)
library(lmerTest) #To get p values must use lmerTest as it uses Satterthwaite's method to approximate them. lme4 does not support this.


df <- read.csv ("beta_caarms_data_COPY.csv") 

head(df)


##############################

#Scatter plot 163 total
ggplot(df, aes(x=x163, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 165 total
ggplot(df, aes(x=x165, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 167 total
ggplot(df, aes(x=x167, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 169 total
ggplot(df, aes(x=x169, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 171 total
ggplot(df, aes(x=x171, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 173 total
ggplot(df, aes(x=x173, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))


#######################################


#Scatter plot 163 pos
ggplot(df, aes(x=x163, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 165 pos
ggplot(df, aes(x=x165, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 167 pos
ggplot(df, aes(x=x167, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 169 pos
ggplot(df, aes(x=x169, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 171 pos
ggplot(df, aes(x=x171, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 173 pos
ggplot(df, aes(x=x173, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#######################################


#Scatter plot 163 neg
ggplot(df, aes(x=x163, y=neg_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Scatter plot 171 neg
ggplot(df, aes(x=x171, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))


############## Total lmer ############################### 


output163 <- lmer(total_1m_21~ drug*x163 + (id| valence), data=df)
summary(output163)

output165 <- lmer(total_1m_21~ drug*x165 + (id| valence), data=df)
summary(output165) 

output167 <- lmer(total_1m_21~ drug*x167 + (id| valence), data=df)
summary(output167) 

output169 <- lmer(total_1m_21~ drug*x169 + (id| valence), data=df)
summary(output169) 

output171 <- lmer(total_1m_21~ drug*x171 + (id| valence), data=df)
summary(output171) 

output173 <- lmer(total_1m_21~ drug*x173 + (id| valence), data=df)
summary(output173) 


############## Pos lmer ############################### 


output163p <- lmer(pos_1m_21~ drug*x163 + (id| valence), data=df)
summary(output163p)

output165p <- lmer(pos_1m_21~ drug*x165 + (id| valence), data=df)
summary(output165p) 

output167p <- lmer(pos_1m_21~ drug*x167 + (id| valence), data=df)
summary(output167p) ##

output169p <- lmer(pos_1m_21~ drug*x169 + (id| valence), data=df)
summary(output169p) 

output171p <- lmer(pos_1m_21~ drug*x171 + (id| valence), data=df)
summary(output171p)

output173p <- lmer(pos_1m_21~ drug*x173 + (id| valence), data=df)
summary(output173p)

############## Neg lmer ############################### 


output163n <- lmer(neg_1m_21~ drug*x163 + (id| valence), data=df)
summary(output163n) ###

output165n <- lmer(neg_1m_21~ drug*x165 + (id| valence), data=df)
summary(output165n) 

output167n <- lmer(neg_1m_21~ drug*x167 + (id| valence), data=df)
summary(output167n) 

output169n <- lmer(neg_1m_21~ drug*x169 + (id| valence), data=df)
summary(output169n)

output171n <- lmer(neg_1m_21~ drug*x171 + (id| valence), data=df)
summary(output171n) ##

output173n <- lmer(neg_1m_21~ drug*x173 + (id| valence), data=df)
summary(output173n)


################## L INSULA ####################### 

#Scatter plot L insula 
ggplot(df, aes(x=L_insula, y=total_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))


ggplot(df, aes(x=L_insula, y=pos_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

ggplot(df, aes(x=L_insula, y=neg_1m_21, shape= drug, color=drug)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=drug))

#Lmer

outputt <- lmer(total_1m_21~ drug*L_insula + (id |valence), data=df)
summary(outputt)


outputb <- lmer(pos_1m_21~ drug*L_insula + (id |valence), data=df)
summary(outputb)
confint(outputb,method="Wald")
r.squaredGLMM(outputb)


outputn <- lmer(neg_1m_21~ drug*L_insula + (id |valence), data=df)
summary(outputn)
confint(outputn,method="Wald")
r.squaredGLMM(outputn)



