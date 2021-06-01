#Full script used in THC meta analysis (Figure 4)


#install.packages ("remotes")
#remotes::install_github ("https://github.com/LCBC-UiO/ggseg.git", build_vignettes = FALSE)
#remotes::install_github("LCBC-UiO/ggseg3d", build_vignettes = FALSE)
#remotes::install_github("https://github.com/LCBC-UiO/ggsegExtra.git", build_vignettes = FALSE)
#install.packages('cowplot')


library(ggseg)
library(ggseg3d)
library(ggsegExtra)
library(dplyr)
library(tidyr)
library(ggplot2)
library(cowplot)



#Cortical effects
cnr1 <- read.csv ("atlas_dk_cnr1.csv")
cnr2 <- read.csv ("atlas_dk_cnr2.csv")
cnresz <- read.csv ("atlas_dk_esz.csv")



p_cnr1 <- ggseg(.data=cnr1, atlas=dk, colour="white", mapping=aes(fill=vari)) +
  labs(fill="CNR1 density") +
  theme(legend.position = "right", legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="black")

p_cnr2 <- ggseg(.data=cnr2, atlas=dk, colour="white", mapping=aes(fill=vari)) +
  labs(fill="CNR2 density") +
  theme(legend.position = "right", legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="black")


cnresz= cnresz %>%
  group_by (Direction)

p_esz <- ggseg(.data= cnresz, atlas=dk, colour= "white", mapping=aes(fill=vari)) +
  labs(fill="Hedge's g") +
  facet_wrap(~Direction, ncol=1) +
  theme(legend.position = "right",   legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="grey") 


cowplot::plot_grid(p_cnr1, p_cnr2, p_esz, ncol =1,
                   labels = c("A", "B", "C"),
                   align = "v", axis = "1")

p_cnr1
p_cnr2
p_esz



#Sub-cortical effects
cnr1_2 <- read.csv ("atlas_dk_2_cnr1.csv")
cnr2_2 <- read.csv ("atlas_dk_2_cnr2.csv")
cnresz_2 <- read.csv ("atlas_dk_2_esz.csv")


p_cnr1_2 <- ggseg(.data= cnr1_2, atlas="aseg", 
      mapping=aes(fill=vari)) +
  labs(fill="CNR1 density") +
  theme(text = element_text(size=18), legend.position = "right",   legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="grey") 

p_cnr2_2 <- ggseg(.data= cnr2_2, atlas="aseg", 
      mapping=aes(fill=vari)) +
  labs(fill="CNR2 density") +
    theme(text = element_text(size=18),legend.position = "right",   legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="grey") 


cnresz_2= cnresz_2 %>%
  group_by (Direction)

p_esz_2 <- ggseg(.data= cnresz_2, atlas="aseg", 
      mapping=aes(fill=vari)) +
  labs(fill="Hedge's g") +
  facet_wrap(~Direction, ncol=1) +
  theme(text = element_text(size=18),legend.position = "right",   legend.direction="vertical", legend.margin = margin(0, 0, 0, 0)) +
  scale_fill_gradientn(colours = c("royalblue","firebrick","goldenrod"),na.value="grey") 


cowplot::plot_grid(p_cnr1_2, p_cnr2_2, ncol =1,
                   labels = c("D", "E"),
                   align = "h", axis = "1")


cowplot::plot_grid(p_esz_2, ncol =1,
                   labels = c("F"),
                   align = "h", axis = "1")

