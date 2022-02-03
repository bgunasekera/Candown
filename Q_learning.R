library(hBayesDM)

df <- read.csv("C:/Users/bjgun/OneDrive - King's College London/CANDOWN/RL_matrix_pstQ.csv")

#SECTION 1 to 4
output <- pst_gainloss_Q( data = df, niter = 2000, nwarmup = 1000, nchain = 4, ncore = 4)

# Visually check convergence of the sampling chains (should look like 'hairy caterpillars')
plot(output, type = "trace")

# Check Rhat values (all Rhat values should be less than or equal to 1.1)
rhat(output)

# Plot the posterior distributions of the hyper-parameters (distributions should be unimodal)
plot(output)

# Show the WAIC and LOOIC model fit estimates
printFit(output)

#%%

#pst_Q model

output2 <- pst_Q( data = df, niter = 2000, nwarmup = 1000, nchain = 4, ncore = 4)
plot(output2, type = "trace")
rhat(output2)
printFit(output2)


