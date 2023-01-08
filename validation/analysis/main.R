setwd("~/Documents/GitHub/younesStrittmatter/dataAnalysis/autoos")


library(lme4)
library(ggeffects)
library(ggplot2)
library(dplyr)
library(tidyverse)
library(cowplot)
library(grid)
library(gridExtra)

error = read.csv('source/error_all.csv')
rouge = read.csv('source/rouge_all.csv')
rouge <- rouge %>% rename_with(str_to_title)
rouge$Translation <- str_to_title(rouge$Translation)

error <- error %>% rename_with(str_to_title)
error$Translation <- str_to_title(error$Translation)

colRegular = "#C5A4CA"
colDerived = "#A4CFA3"
colCrossing = "#9BBAD3"
colConstraints = "#E68F90"


rouge <- rouge %>% filter(Translation != "Segmenting")
rouge <- rouge %>% filter(is.na(Nr_crossing) | Nr_crossing < 2)
#rouge$Translation <- factor(rouge$Tanslation, levels = c("Regular", "Derived", "Crossing", "Constraints"))

error <- error %>% filter(Translation != "Segmenting")
error <- error %>% filter(Translation != "Constraints")
error <- error %>% filter(is.na(Nr_crossing) | Nr_crossing < 2)

#error$Translation <- factor(error$Tanslation, levels = c("Regular", "Derived", "Crossing", "Constraints"))

modelRouge <- lm(Rouge1.Fmeasure. ~ Complexity + Translation, data = rouge)
summary(modelRouge)

y = ggpredict(modelRouge, terms = c('Complexity[all]', 'Translation'), type = 're')
attr(y, "title") = 'Text Similarity'
attr(y, "y.title") = 'ROUGE-L f-measure'
attr(y, "x.title") = 'Code Elements'

plt_rouge = plot(y) + 
  scale_color_manual(values = c(colRegular, colDerived, colCrossing, colConstraints)) +
  scale_fill_manual(values=c(colRegular, colDerived, colCrossing, colConstraints)) +
  theme(text=element_text(family="Arial"), plot.title = element_text(face='bold',hjust = 0.5, margin = margin(t = 0, r = 0, b = 10, l = 0, unit = "pt"))) +
  guides(color = FALSE, fill = FALSE)

plt_rouge_dummy = plot(y) + 
  scale_color_manual(values = c(colRegular, colDerived, colCrossing, colConstraints)) +
  scale_fill_manual(values=c(colRegular, colDerived, colCrossing, colConstraints))



modelError <- glm(Accuracy ~ Complexity + Translation, data = error, family = 'binomial')
summary(modelError)

y_1 = ggpredict(modelError, terms = c('Complexity[all]', 'Translation'), type = 're')
attr(y_1, "title") = 'Code Accuracy'
attr(y_1, "y.title") = 'Accuracy'
attr(y_1, "x.title") = 'Code Elements'
#png('rouge.png', width=2400,height=2000,res=640)
plt_error = plot(y_1) + 
  scale_color_manual(values = c(colRegular, colDerived, colCrossing, colConstraints)) +
  scale_fill_manual(values=c(colRegular, colDerived, colCrossing, colConstraints)) +
  theme(text=element_text(family="Arial"), plot.title = element_text(face='bold',hjust = 0.5, margin = margin(t = 0, r = 0, b = 10, l = 0, unit = "pt"))) +
  guides(color = FALSE, fill = FALSE)

legend <- cowplot::get_legend(plt_rouge_dummy)

# Plot the legend on its own
plt_legend <- plot(legend)



# Convert the plot to a grob


# Add the letter
text_grob_A <- textGrob("A", x = unit(0, "npc"), y = unit(1, "npc"), 
                      just = c("left", "top"), 
                      gp = gpar(fontsize = 15))
text_grob_B <- textGrob("B", x = unit(0, "npc"), y = unit(1, "npc"), 
                        just = c("left", "top"), 
                        gp = gpar(fontsize = 15))

grid <- plot_grid(text_grob_A, plt_error, NULL, text_grob_B, plt_rouge, NULL, legend, NULL, nrow=1, rel_widths = c(0,3,.2,0,3,.2,1.2,0))
png('both.png', width=2400,height=1000,res=410)
grid
dev.off()
