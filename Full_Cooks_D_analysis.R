#Easy script for Cooks D outlier analysis: Allows identification of outliers via a plot. Also creates a new data frame for easy re-analysis without the outliers.
#https://stats.stackexchange.com/questions/164099/removing-outliers-based-on-cooks-distance-in-r-language 
#NOTE: Only lines 5 to 17 are of real interest. 20 onwards are more application examples

# Plot of data with outliers
cooksd <- cooks.distance(Stat_model_with_possible_outliers) #in brackets insert lm/lmer/stat model of choice

sample_size <- nrow(df) #in brackets insert data frame used for stat model
plot(cooksd, pch="*", cex=2, main="Influential Obs by Cooks distance")  # plot cook's distance
abline(h = 4/sample_size, col="red")  # add cutoff line
text(x=1:length(cooksd)+1, y=cooksd, labels=ifelse(cooksd>4/sample_size, names(cooksd),""), col="red")  # add labels


# Removing Outliers
influential <- as.numeric(names(cooksd)[(cooksd > (4/sample_size))])

df_NoOutliers <- df[-influential, ]


#Plot and lmer RT no outliers
ggplot(df_NoOutliers, aes(x=X_variable, y=Y_variable, color=Grouping_variable)) +
  geom_point()+
  geom_smooth(method=lm, aes(fill=Grouping_variable))+
  theme_light()+
  labs(tag= "A", x = "X Label", y = "Y Label", color = "Grouping Label")

lmer_NoOutliers <- lmer(XXX), data=df_NoOutliers) #Customise this to match the "Stat_model_with_possible_outliers" used in line 5
summary(lmer_NoOutliers) #summary data
confint(lmer_NoOutliers,method="Wald") #confidence interval
r.squaredGLMM(lmer_NoOutliers) #r squared

